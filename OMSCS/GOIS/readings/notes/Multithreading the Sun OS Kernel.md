## Multithreading the Sun OS Kernel

### Multithreading the Sun OS Kernel

#### Abstract

----

* Using threads makes the kernel fully preemptible and capable of real-time response

#### Introduction

----

* support multiprocessors in SunOS; go further than just adding locks
* support more than one thread of control within a user process
* capable of low latency / user-level multithreading

#### Overview of the Kernel Architecture

----

* Kernel Threads are lightweight
	* small data structure and stack
	* switching does not require changing virtual memory address
	* fully preemptible
* Kernel Threads are used to:
	* provide asynchronous kernel activity
		* remove diversions in the idle loop and trap code
		* replaces them with independently scheduled threads
	* interrupts are also handled by kernel threads
	* support of multiple kernel-supported threads of control
		* LWPs = lightweight processes
		* while all LWPs have a kernel thread, not all kernel threads have an LWP
	* user-level library
		* uses LWPs to implement user-level threads
		* scheduled at user-level and switched by the library to any of the LWPs belonging to the process
		* bound to a particular LWP
		* user-level threads can be switched between without entering the kernel
		* allows a user process to have thousands of threads without overwhelming kernel resources

#### Data Structures

---

* Traditionally, `user` and `proc` structures contained all kernel data for a given process
* The new kernel separated the data into data associated with each LWP and its kernel thread
* Per-process data is contained in the `proc` structure and contains a list of:
	* kernel threads associated with the process
	* pointer to the process address space
	* user credentials
	* list of signal handlers
* The LWP structure contains:
	* PCB (Process Control Block)
		* processor registers
		* system call arguments
		* signal handling masks
		* resource usage info
		* profiling pointers
	* Pointers to the kernel thread and process structures
* The Kernel Thread structure contains:
	* kernel registers
	* scheduling class
	* dispatch queue links
	* pointers to the stack and associated LWP, process, and CPU structures
* Per-processor data is kept in the `cpu` structure
	* contains pointers to the currently executing thread, idle thread, dispatching and interrupt handling information
* To speed access to the thread, LWP, process, and CPU structures, there is a global register (%g7) that points to the current thread structure

#### Kernel Thread Scheduling

-----

* A scheduling class determines the relative priority of processes within a class and converts it to a global priority
	* The scheduling class and dispatcher operate on threads instead of processes
	* Three Scheduling classes in SPARC
		* system
		* time-share
		* real-time (Fixed Priority)
* The dispatcher choose the thread with the greatest global priority
	* If there are two with the same priority, they are dispatched in round robin order
* By making the kernel preemptible, the real-time class and interrupt threads are better supported

#### System Threads

---

* Can be created for short and long term activities
* Scheduled like any thread but belong to system scheduling class
* No need for LWP structure so the thread and stack are allocated together in a non-swappable area
* The segment driver, `seg_kp` handles stack allocations
	* Also handles virtual memory allocations for the kernel and provides "red zones" to protect stack overflows

#### Synchronization Architecture

---

* Kernel uses same synchronization objects as the user-level libraries
	* Mutex (Mutual Exclusion Locks)
	* Condition variables
	* Semaphores
	* multiple readers
	* single writer (reader/writer) locks
* The synchronization object is specified when it is initialized
* Synchronization options take a pointer to the object as an argument
* Most objects allow for collecting statistics
* Most synchronization primitives prevent thread from getting past the primitive until some condition is satisfied
	* Sleep
	* Spin
	* Other
* By default, kernel thread synchronization primitives can _potentially_ sleep
* Some synchronization primitives are "_strictly bracketing_" which means the thread that locks a mutex, must be the one that unlocks it
* Some synchronization primitives are intended for use where they may block for long or indeterminant periods
	* `cv_wait_sig()`
	* `sema_p_sig()`
		* These allow blocking to be interrupted by reception of a signal
		* Once a signal is received, the caller must release any resources and return

#### Mutual Exclusion Lock Implementation

---

* Mutexes are the most commonly used primitive
	* Usually held for short intervals
		* So don't wait for Disk I/O while using this
	* Not recursive (cannot call `mutex_enter()` once already entered)
	* Thread that holds a mutex must release the mutex
		* These rules help to avoid deadlocks
* If `mutex_enter` cannot set an already set lock, the blocking action taken will depend on the mutex type that was passed to `mutex_init()`
	* The default blocking policy is called _adaptive_
		* type `MUTEX_DEFAULT`
		* spins while the owner of the lock remains running
			* Done by polling the owner's status
			* If the owner stops running, the caller stops spinning and sleeps
			* Gives fast response and low overhead
* Spin mutexes are another type (`MUTEX_SPIN`)
	* Rarely used as adaptive mutex is more efficient
* Device drivers have their own mutex type, `MUTEX_DRIVER`
* `mutex_enter()` for adaptive mutexes
	* non-adaptive mutexes use a separate primitive lock field in the mutex data structure
		* So, it can always try to apply an adaptive lock first, and if that fails, consider the mutex may be another type

#### Turnstiles Vs Queues in Synchronization Objects

---

* Each object needs way to find threads that are suspended and waiting for that object
* To reduce storage cost of synchronization objects, the queue header is not in the object, but rather preallocated.
	* Therefore the header information is stored as two bytes pointing to a turnstie structure containing the sleep queue header and priority inheritnace information
* Alternatively, the sleep queue can be sleected using a hash function on the address of the synchronzation object
	* `sleep()` uses this approach in a traditional kernel
* That said, the turnstile approach is favored for more predictable real-time behaviour since they are never shared by other locks

#### Interrupts as Threads

---

* Various implementations have various synchronization primitives
* For mutexes, spin primitives must hold the interrupt priority high enough to prevent interrupt handlers from using the synchronization object while it is locked (causing a deadlock)
	* The interrupt level must be raised before the lock is acquired and lowered after the lock is released
* Drawbacks of this Approach
	* Raising and lowering is an expensive operation
	* Many subsystems are interdependent and the mutexes must protect themselves at a fairly high interrupt level
	* Interrupt handlers must avoid use of kernel functions that can potentially sleep, even for short periods
* To avoid the above drawbacks
	* interrupts are asynchronously created and dispatched high-priority threads
		* This allows them to sleep and use the standard synchronization primitives
* Putting threads to sleep must be done in software
	* For this reason, this section of code is bounded and cannot be interrupted
* Traditional UNIX kernels protect the dispatcher by locking out interrupts
* But the restructured kernel has a level above which interrupts are handled more like firmware.
	* If the thread level is set to max, then all interrupts are locked out during dispatching.

#### Implementing Interrupts as Threads

---

* Previous SunOS versions worked like UNIX - once an interrupt occurs the interrupted process is _pinned_ until the interrupt returns
* In SunOS 5.0, interrupts behave like asynchronous threads
	* Interrupt threads are preallocated and partly initialized
	* When an interrupt occurs, the minimum amount of work is done to move on to the stack of an interrupt thread and set it as the current thread
	* At this point, the interrupt thread is not a full-fledged thread (can't be descheduled) and the interrupted thread is _pinned_ until the interrupt thread returns or blocks
	* When the interrupt returns, the interrupted thread state is restored
* Interrupts may nest - an interrupt thread my be interrupted!
* If an interrupt thread blocks on a synchronization variable (mutex or condition), it saves state (_passivates_) and becomes a full-fledged thread, capable of being run by the CPU, and then returns to the pinned thread.
* While interrupt threads are in progress its interrupt level and all lower priority interrupts are blocked
	* If the thread blocks, normal interrupts must be disabled in case the interrupt handler is not reenterable or is doing high-priority processing
	* While blocked, the interrupt thread is bound to a particular processor (the one it stared on)
		* A flag is set in the CPU to indicate an interrupt at that level has blocked and the minimum interrupt level is noted
		* When the interrupt level changes, the base interrupt level is checked and the interrupt priority level is not allowed below that
* When `release_interrupt()` is called, it saves the state of the pinned thread and clears the interrupt indication which allows the CPU to lower the interrupt priority level
* Alternatively, we can use _bounded first-level interrupt handlers_ to capture device state, whatever that means….
	* But this requires device drivers to be restructured and a full context switch

##### Interrupt Thread Cost

* Taking an interrupt costs 40 SPARC instructions
* Savings in mutex enter/exit is 12 instructions
	* But mutexes are much more frequent
* There is also a memory cost
	* An interrupt thread is preallocated for each potentially active interrupt level below the thread level
	* An additional interrupt thread is preallocated for the clock (one per system)
	* Each thread requires a stack and data structure of about 8KB so the memory cost can add up
	* But since it is unlikely all interrupt levels will be active, we can have a smaller pool of threads and block all interrupts below the thread level when the pool is empty

##### Clock Interrupt

* The clock interrupt is handled specially as there is only one in the whole system (not per CPU)
* The clock interrupt invokes the clock thread only if it is not already active
* The clock thread can be delayed due to blocking on a mutex or higher level interrupt
	* If the clock tick occurs and the clock thread is already active, the interrupt is cleared and a counter is incremented
	* If the clock thread finds a non-zero counter it decrements the counter and repeats the clock processing
		* Rare in practice though

#### Kernel Locking Strategy

---

* The Kernel uses data-based blocking
	* This meands the mutex and reader/writer locks protect a set of shared data as opposed to protecting routines (monitors)
		* Every piece of shared data is protected by a synchronization object

#### Non-MT Driver Support

---

* Some drivers have not been written to protect themselves against concurrency in a multithreaded environment
	* They are called _MT-unsafe_ as they don't provide their own locking
* So, they have provided wrappers that acquire a single global mutex called `unsafe_driver`
	* This ensures only one such driver is in use at a time
* Every entry point for a driver must acquire the `unsafe_driver` mutex.
* MT-unsafe drivers can also use the old sleep/wakeup mechanism
	* `sleep()` safely releases the `unsafe_driver` mutex after the thread is asleep and reacquires it before returning
	* `longjmp()` is also maintained
		* NOTE: I don't understand the next part so I left it out of my notes
	* `sleep()` checks to make sure it is called by an MT-unsafe driver and panics if it isn't
		* Don't use `sleep()` with a driver that does its own locking
	* Drivers that do their own locking are called _MT-safe_
	* _MT-hot_ refers to drivers that do fine-grained locking

#### SVR4/MP DKI Locking Primitives

---

* SvR4/MP DKI is a standard used by UNIX
	* SunOS implements the same interfaces but uses its own internal mechanisms
		* This allows for easier porting

#### Kernel Time Slicing

---

* Clock interrupt handler preempts a thread
	* Allows single processor systems to have arbitrary code interleaving
	* By increasing the rate of preemption, the developers were able to find locking problems even before multiprocessor architectures were available
		* Only use as a debugging feature

#### Lock Hierarchy Violation Detection

---

* The developers created a static analysis tool called _locknest_ that checks for lock ordering violations
* Valuable in debugging deadlocks

#### Deadlock Detection

---

Deadlocks caused by hierarchy violations are usually detected at run time, and on locks held for writes, but lock held for reads is harder as there is not complete list of threads holding a read lock. Condition variable deadlocks aren't detected

#### Summary

---

* SunOS 5.0 is:
	* Fully preemptible, real-time kernel
	* Highly concurrent on symmetric multiprocessors
	* Support for user threads
	* Interrupts handled as independent threads
	* Adaptive Mutual Exculsion Locks
* Threads in the kernel and user level are almost identical
* Threads in the kernel is mostly positive, but can be overused - there is a cost
	* The stacks are large and must be allocated on separate pages
	* Context switching is still expensive
	* Callouts and other "zero-weight" processes are still useful, but threads "provide a nice strcuturing paradigm for the kernel"
