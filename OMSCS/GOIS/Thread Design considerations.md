# Preview
- Kernel vs. user-level threads
- Threads and interrupts
- Threads and signal handling

# Kernel vs. User Level Threads
![[Pasted image 20230904160322.png]]
# Thread Data Structures: Single CPU
![[Pasted image 20230904161801.png]]
- For multi-thread cases
	- we breaks the info in PCB into KLT for each thread
	- The PCB will still contain info of virtual address mapping for the whole process warped in user level
	- Thread_lib will contain info for each user-level thread (ULT)

# Thread Data Structures: At Scale![[Pasted image 20230904162643.png]]
# Hard and Light Process State
![[Pasted image 20230904195922.png]]
- split information originally in PCB
	- hard process state contains all user-level threads that execute within that process
	- light process state contains user-level threads that are associated with kernel level threads
# Rationale for Data Structures
- Single PCB
	- characteristics
		- large continuous data structure
		- private for each entity
		- saved and restored on each context switch
		- update for any changes
	- cons
		- scalability
		- overheads
		- performance
		- flexibility
- Multiple data structures
	- characteristics
		- smaller data structures
		- easier to share
		- on context switch only save and restore what needs to change
		- user-level library need only update portion of the state
	- pros
		- scalability
		- overheads
		- performance
		- flexibility
# User Level Structures in Solaris 2.0
![[Pasted image 20230905203950.png]]
- LWP == Light Weight Process
- CPU == Central Processing Unit
- Implementing lightweight threads by Stein & Shah
	- not POSIX threads, but similar
	- thread creation => thread ID(tid)
		- tid => index into table of pointers
		- table pointers point to per thread data structure
	- stack growth can be dangerous
		- solution => red zone![[Pasted image 20230905204503.png]]
# Kernel Level Structures in Solaris 2.0
- process
	- list of kernel-level threads
	- virtual address space
	- user credentials
	- signal handlers
- light-weight process (LWP) - relevant info of a subset of process
	- user- level registers
	- system call args
	- resource usage info
	- signal mask
	- similar to ULT, but visible to kernel to kernel 
	- not needed when process not running
- kernel-level threads
	- kernel-level registers
	- stack pointer
	- scheduling info
	- pointers to associated LWP, process, CPU structures
	- info needed even when process not running => not swappable
- CPU
	- current thread
	- list of kernel-level thread
	- dispatching & interrupt handling info
	- on SPARC dedicated reg == current thread
![[Pasted image 20230905211332.png]]
# Basic Thread Management Interaction
- Request additional kernel-level thread![[Pasted image 20230905212622.png]]
- When kernel-level threads are blocked
	- ![[Pasted image 20230905212831.png]]
	- Kernel does not know what is happening in user-level library![[Pasted image 20230905213033.png]] 
- System calls and special signals allow kernel and ULT library to interact and coordinate
# Thread Management Visibility and Design
## Lack of Thread Management Visibility
- Kernel sees
	- KLTs
	- CPUs
	- KL scheduler
- UL library sees
	- ULTs
	- available KLTs
-  1-1 mapping KLT - ULT![[Pasted image 20230906144033.png]]
- Many-Many KLT -ULT mapping![[Pasted image 20230906144415.png]]
	- other ULTs can only be executed when the preempted KLT is back
- Problem
	- Visibility of state and decisions between kernel and UL library
	-  Kernel level library is not ware of Many to Many cases:
		- UL scheduling decisions
		- change ULT - KLT mapping
		- mutex variables and wait queues
	- 1-1 helps address some of these issues 
## How / When  does the UL library run?
- Process jumps to UL library scheduler
	- ULTs explicitly yield
	- timer set by UL library expires
	- ULTs call library functions like lock / unlock
	- blocked thread become runnable
	- runs on ULT operations
	- runs on signals from timer or kernel
# Issues on Multiple CPUs
![[Pasted image 20230906201400.png]]
- We need to switch the kernel level thread bound to T1 with T3
- ![[Pasted image 20230906201447.png]]
- ![[Pasted image 20230906201526.png]]
# Synchronization-Related Issues
- ![[Pasted image 20230906202156.png]]
- Adaptive mutexes:
	- if critical section short => don't block ! spin!
	- for long critical sections default blocking behavior
- Destroying Threads
	- Instead of destroying ... reuse threads
	- when a thread exits
		- put a "death row"
		- periodically destroyed by reaper thread
		- otherwise thread structures / stacks are reused => performance gained
# Interrupts and Signals Intro![[Pasted image 20230906203545.png]]
- Interrupts v.s. signals
	- Interrupts
		- events generated externally by components other than the CPU (I/O devices, timers, other CPUs)
		- determined based on the physical platform
		- appear asynchronously
	- Signals
		- events triggered by the CPU & software running on it
		- determined based on the operating system
		- appear synchronously or asynchronously
	- have a unique ID depending on the hardware or OS
	- can be masked and disabled / suspended via corresponding mask
		- per-CPU interrupt mask. per-process signal mask
	- if enabled, trigger corresponding handler
		- interrupt handler set for entire system by OS
		- signal handlers set on per process basis, by process
# Interrupt Handling
![[Pasted image 20230906204641.png]]
# Signal Handling
![[Pasted image 20230906204836.png]]
- Handler / Actions
	- Default Actions
		- Terminate, 
		- Ignore
		- Terminate and Core Dump
		- Stop / Continue
	- Process Installs Handler
		- signal(), sigaction()
		- for most signals, some cannot be "caught"
	- Examples![[Pasted image 20230906205228.png]]
# Why Disable Interrupts or Signals
- Deadlock
	- keep handler code simple
		- too restrictive
	- control interruptions by handler code
		- user interrupt / signal masks
		- ![[Pasted image 20230906210000.png]]
# More on Signal Masks
- Interrupt mask
	- if mask disables interrupt, hardware interrupt routing mechanism will not deliver interrupt to CPU
- Signal masks
	- are per execution context
	- if mask disables interrupt, kernel sees mask and will not interrupt routing corresponding thread
# Interrupts on Multicore Systems
- Interrupts can be directed to any CPU that has them enabled
- May set interrupt on just a single core
	- avoids overheads & perturbations on all other cores
# Types of Signals
- one-shot signals
	- "n signals pending == 1 signal pending"