## Implementing Lightweight Threads

### Implementing Lightweight Threads

#### Introduction

---
- Threads Library Implementation
	- Lightweight but allow fully concurrent access to system resources
	- User threads multiplex on a pool of kernel-supported threads
	- Includes threads library and a modified kernel to support multiple threads in a single UNIX process

#### Threads Model

---
- Traditionally, UNIX processes had a single thread
- SunOS Multi-thread Architecture allowed for more than one thread
- Threads are viewed as execution resources that can be applied to solving the problem at hand
- Threads share process instructions and most of its data
- A change in shared data can be seen by the other threads in the process
	- Ex. One thread opens a file, another can read from it
- Synchronization Facilities
	- Mutex Locks
	- Condition Variables
	- Semaphores
	- Multiple Readers / Single Writers locks
- Synchronization variables are allocated in ordinary memory
- Threads in different processes can synchronize via synchronization variables in shared memory or mapped files
	- These variables must be marked as being process-shared when they are initialized
	- They may have different variants with different blocking behavior
- Each thread has its own program counter (PC) and stack to keep track of local variables and return addresses
- Each thread can make arbitrary system calls and interact with processes
- NOTE: If one thread calls `exit()` all threads are destroyed
- Each thread has its own signal mask
	- This allows blocking asynchronously generated signals while accessing a state modified by a signal handler
	- Synchronously generate signals such as `SIGSEGV` are sent to the thread that caused them
	- Externally generated signals are sent to one of the threads that has it unmasked
		- If all threads mask a signal, it is set to pending until a thread unmasks it
		- Signals can also be send to particular threads in the same process
		- The number of signals received by the process is less than or equal to the number sent
- All threads within a process share the set of signal handlers
	- If the handler is set to `SIG_IGN` any received signals are discarded
	- If the handler is set to `SIG_DFL` the default action (ex. stop, continue, exit) applies to the process as a whole
- Processes can fork in one of two ways
	- The first clones the entire process and all of its threads
	- The second only reproduces the calling thread in the new process
		- This is useful when the process is going to call `exec()`

#### Threads Library Architecture

---
- Threads are the programmer's interface for multi-threading
- LWP (LightWeight Processes) can be thought of as a virtual CPU
- Each LWP is separately dispatched by the kernel onto the available CPUs according to scheduling class and priority
- The threads library schedules threads on a pool of LWPs in the same way the kernel schedules LWPs on a pool of processors
- Threads are simply data structures and stacks maintained by the library
- The thread library can start and stop threads without involving the kernel
	- Also, create, destroy, block, activate etc without the OS getting involved
- LWPs are more expensive than threads as each one uses kernel resources
- Note: only a few threads need to be active at the same instant
- Some threads must be visible to the system, for example, when a real-time response in needed such as for a mouse tracking thread
	- This is accomplished by binding the thread to be permanently bound to an LWP
- Most programmers use threads and don't worry about LWPs

#### LWP Interfaces

---
- Similar to threads
	- Share most process resources
	- Has private set of registers and a signal mask
	- Have attributes unavailable to threads
		- Kernel-supported scheduling class, virtual time timers, alternate signal stack, and profiling buffer
- `_lwp_create()` creates another LWP within the process
- `_lwp_makecontext()` creates a machine context that emulates the standard calling sequence to a function
	- This context can then be passed to `_lwp_create()`
	- This gives some measure of machine independence
- LWP synchronization interfaces use mutex locks, condition variables, and counting semaphores
- These routines only enter the kernel if necessary
- LWP synchronization variables are placed in memory by the application
	- if placed in shared memory or mapped files, they are accessible to other processes
	- Using memory mapped files allows synchronization variables and shared data to be preserved in a file
		- the application can then be restarted and resume execution without initialization
- When a LWP synchronization primitive causes the calling LWP to block, it is suspended on a kernel-supported sleep queue associated with the offset in the mapped file or shared memory segment
	- This allows LWPs in different processes to synchronize despite having different virtual memory
- `_lwp_getprivate()` and `_lwp_setprivate()` provide one pointer's worth of storage that is usually used to point to the thread's data structure (on SPARC this is register `%g7`)
- Alternatively, we could have a private memory page for each LWP which requires more kernel effort and more memory
	- But, this is useful on register-constrained machines or machines where registers are not reserved to the system
- Two additional signals:
	- `SIGLWP` Used as in inter-LWP signal mechanism using the `_lwp_kill()` interface
	- `SIGWAITING` Generated by the kernel when all LWPs in a process have been blocked in indefinite waits
		- Used by threads package to ensure processes don't deadlock indefinitely

#### Threads Library Implementation

---
- Thread structure:
	- thread ID
	- area to save execution context
	- thread signal mask
	- thread priority
	- pointer to the thread stack
- Thread stack storage is either automatically allocated by the library or passed in by the application on thread creation
- Library allocated stacks are obtained by mapping pages in memory
	- The page following the stack is invalid to protect from overruns (red zone)
- When a thread is created a thread ID is assigned
	- The ID is an index in a table of pointers to thread structures
	- provide meaningful errors

#### Thread-local Storage

---
- Private storage for each thread
	- Used for thread-private data
- The thread structures and `errno` is allocated in TLS
- TLS is obtained via a new `#pragma` called `unshared` that is supported by the compiler and linker
- TLS is zeroed initially (static initialization is not allowed)
- The linker determines the size of the TLS
	- `_etls` represents the size of the TLS
- After a program starts, the size of TLS is fixed
- On SPARC global register `%g7` is assumed to point to the base address of TLS

#### Thread Scheduling

---
- When a thread is scheduled it is assigned to an LWP in a pool
	- It then has all the attributes of a kernel-supported thread
- Thread priorities range from 0 to infinity
	- priority is fixed in the sense the library sets it, but it can be altered by the thread itself, or another thread in the same process
		- This priority is not known to the scheduler
- An LWP is either idling or running a thread
	- When it is idle it waits on a synchronization variable
	- When a thread is made runnable, it is added to the dispatch queue and an idle LWP is awakened
		- the LWP wakes up and switches to the highest priority thread on the dispatch queue
		- If blocked, the thread is put to sleep and switches to the highest priority on the dispatch queue
		- If the queue is empty, the LWP goes back to idle
		- If all LWPs are busy, the thread stays on the dispatch queue until an LWP becomes available

##### Thread States and the Two Level Model

- An unbound thread can be in one of five different states:
	- RUNNABLE
	- ACTIVE
	- SLEEPING
	- STOPPED
	- ZOMBIE
- Interestingly, a thread's LWP can have one of multiple states:
	- RUNNING
	- SLEEPING
	- STOPPED
	- WAITING

##### Idling and Parking

- When there are no more RUNNABLE threads, the LWP switches to the idle stack and waits on the global LWP condition variable
- When another thread becomes RUNNABLE the global condition is signaled and an idling LWP awakes and tries to run any RUNNABLE threads
- When a bound thread blocks a process-local synchronization variable, its associated LWP also stops running
	- This is done through the use of a semaphore and the LWP is now _parked_
- When an unbound thread becomes blocked and no more RUNNABLE threads
	- LWP parks itself on semaphore rather than idling on stack and global condition variable
	- avoid context switch

##### Preemption

- Threads compete for LWPs based on priority
- A queue of active threads is maintained and if a RUNNABLE thread has a higher priority than an active thread, then the thread is removed from the queue and preempted from its LWP
- Two cases when preempt is needed:
	- A newly RUNNABLE thread has a higher priority than the lowest active thread
	- The priority of an ACTIVE thread is lowered below that of the highest priority RUNNABLE thread
- ACTIVE threads are preempted by setting a flag and sending its LWP a SIGLWP.

##### The Size of the LWP Pool

- The threads library adjusts the size
	- Can't allow deadlock due to lack of LWPs
	- Must make efficient use of LWPs
		- We don't create one per thread as most would be idle and wasting resources
	- When the number of threads exceeds the number of LWPs, the threads library installs a handler for SIGWAITING and if there are RUNNABLE threads, creates a new LWP and adds it to the pool
	- It is possible to computer a weighted time average and adjust, but it's not certain if the costs outweigh the benefits
- Applications can inform the threads library about their expected concurrency using `thr_setconcurrency()`
- Occasionally, the number of LWPs can grow to be larger than the number of threads. In this case, the library prunes old LWPs, typically those over 5 minutes

#### Mixed Scope Scheduling

---
- Bound and unbound threads can exist in the same process
- A bound thread in the real-time class can take precedence over the other threads
- Detached threads (bound or unbound) are put into a queue called `deathrow` and the state is set to ZOMBIE.
- The thread library has special thread called reaper that clears out the ZOMBIE processes
	- Runs when there are idle LWPs or when `deathrow` gets full
- Need to find a good balance between running reaper too often and not often enough

#### Thread Synchronization

---
- Two basic types of synchronization variables
	- process-local (default)
	- process-shared
- Process-local synchronization Variables
	- Default blocking behavior is to put the thread to sleep
	- Each synchronization variable has a sleep queue associated with it
		- If a thread is unbound, the scheduler dispatches another thread to its underlying LWP
		- If it is bound, it stay permanently bound to its LWP so the LWP is _parked_ on its thread
	- Blocked threads are awakened when the synchronization variables become available
	- Blocked threads are removed from the synchronization variable's sleep queue and is dispatched by the scheduler
	- If the thread is bound, the scheduler unparks it so its LWP is dispatched by the kernel
	- For unbound threads, the thread is placed on a run queue based on its priority
- Process-shared Synchronization Variables
	- These are placed into memory accessible by multiple processes so threads can be synchronized
	- Must be initialized when created
		- When initialized, they are marked as process-shared
		- This allows for the correct blocking behaviour
			- LWP synchronization primitives put blocking threads to sleep in the kernel still attached to LWPs and correctly synchronize between processes

#### Signals

---
- Problem is that signals are sent by the kernel, but user-level threads are invisible to it
	- Signal delivery is dependent upon the thread signal mask
- A goal is to provide cheap async safe synchronization primitives
	- A function is async safe if it is reentrant with respect to signals
	- Low overhead safe synchronization primitives are crucial for multithreaded libraries

#### Signal Model Implementation

---
- One strategy is for LWPs to reflect the thread's signal mask
- This allows the kernel to directly choose a thread from the ACTIVE threads
	- Problem is threads are rarely ACTIVE
	- Also, threads that are asleep will not receive signals
	- Also, a system call is necessary when switching between threads with different masks which is expensive
- The problems above can be solved if LWP signal masks and ACTIVE thread masks are treated independently
	- A process can receive a set of signals equal to the intersection of all the thread signal masks
	- The library makes sure the LWP signal mask is equal to or less restrictive than the thread mask
- There is a global handler mechanism to prevent signals from reaching interrupted threads
	- There's a lot more detail on Page 7 - read it if you're interested.

##### Sending a Directed Signal

- A thread can send a signal to another thread in the same process using `thr_kill()`
	- If the tread is not ACTIVE, the signal is posted in a pending signals mask
		- When execution is resumed, the thread receives pending signals

#### Signal Safe Critical Sections

---
- To prevent deadlock in the presence of signals, critical sections should be safe with respect to signals. All asynchronous signals should be masked during these sections
- To do this, the threads library as `thr_sigsetmask()`. If signals don't occur, it does not, there is no system call which makes it as fast as modifying the user-level thread signal mask
- The threads library also sets a special flag when it enters or exits a critical section

#### Debugging Threads

---
- The normal kernel-supported debugging interface (`/proc`) does not work well with threads.
	- Instead, there is a special debugging library that the debugger links to using `dlopen()`
		- All thread specific knowledge is in the thread debugging library
