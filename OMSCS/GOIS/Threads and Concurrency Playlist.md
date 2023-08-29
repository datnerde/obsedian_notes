![[Pasted image 20230827125300.png]]
# Visual Metaphor
>[!quote]
> A thread is like a worker in a toy shop
* is an active entity
	* executing unit of a process
* works simultaneous with others
	* many threads executing
* requires coordination
	* sharing of I/O devices, CPUs, memory
# Process v.s. Thread
![[Pasted image 20230827130011.png]]
# Benefits of Multithreading
- Parallelization => Speed UP
- Specialization => Hot Cache!
- Efficiency => lower memory management requirement& cheaper IPC

# Benefits of Multithreading:  # threads > # CPUs
![[Pasted image 20230827171717.png]]
- if (t_idle)>2*(t_ctx_switch) then context switch to hide idling time
- t_ctx_switch threads < t_ctx_switch processes
	- because threads are in a shared address space even in a single CPU
- hide latency
# Benefits of Multithreading: Apps and OS
![[Pasted image 20230827172036.png]]
# Basic Thread Mechanisms
- What we need to support thread?
	- thread data structure
		- identify threads, keep track of resources
	- mechanisms to create and manage threads
	- mechanisms to safely coordinate among threads running concurrently in the same address space
- Concurrency Control & Coordination![[Pasted image 20230827201858.png]]
	- mutual exclusion
		- exclusive access to only one thread at a time
		- mutex
	- wait on other threads
		- specific condition before proceeding
	- waking up other threads from the wait stage
# Thread Creation
- Thread type
	- thread data structure ![[Pasted image 20230827202600.png]]
- Fork (proc, args)
	- create a thread
	- not UNIX fork
- Join (thread)
	- terminate a thread
- ![[Pasted image 20230827203156.png]]
# Mutual Exclusion
- Mutex
	- It is like a Lock![[Pasted image 20230827204823.png]]
	- Critical Section: The portion of code protected by the Mutex
	- ![[Pasted image 20230827205302.png]]
# Condition Variable
![[Pasted image 20230827213108.png]]
- use the Signal to notify wait function for consumer to modify the list when it is full
# Condition Variable API
- Condition type data structure
- Wait (mutex, cond)
	- mutex is automatically released and re-acquired on wait
- Signal (cond)
	- notify only one thread waiting on condition
- Broadcast (cond)
	- notify all waiting thread
- Why we use while instead of i ![[Pasted image 20230827213837.png]]

# Reader/Writer Problem
- Problem Description
![[Pasted image 20230827215254.png]]
- Example Code![[Pasted image 20230828210205.png]]![[Pasted image 20230828210632.png]]
- General Structure![[Pasted image 20230828210229.png]]
- Conceptual Critical Section![[Pasted image 20230828210618.png]]
- Critical Section Structure with Proxy Variable![[Pasted image 20230828210900.png]]
	- By pass the limitation of mutex so that we can perform more complicated operation
# Common Pitfalls
- keep track of mutex / cond. variables used with a resource
	- e.g., mutex_type 
- check that you are always (and correctly) using lock & unlock
	- e.g., did you forget to lock / unlock? what about compilers?
- use a single mutex to access a single resources!
- check that you are signaling correct condition
- check that you are not using signal when broadcast is needed
	- signal: only 1 thread will proceed ... remaining threads will continue to wait ... possibly indefinitely
- ask yourself: do you need priority guarantees?
	- thread execution order not controlled by signals to condition variables
- spurious wake ups![[Pasted image 20230828212126.png]]
	- when we wake threads up knowing they may not be able to proceed
	- can we unlock the mutex before broadcast / signal?![[Pasted image 20230828212344.png]]
	- We can do it on writer but not reader![[Pasted image 20230828212450.png]]
- dead locks
	- two or more competing threads are waiting on each other to complete, but none of them ever do