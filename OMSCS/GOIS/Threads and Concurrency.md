## Threads and Concurrency

![[Pasted image 20230827125300.png]]

### Visual Metaphor

> [!quote]  
> A thread is like a worker in a toy shop

* is an active entity
	* executing unit of a process
* works simultaneous with others
	* many threads executing
* requires coordination
	* sharing of I/O devices, CPUs, memory

### Process v.s. Thread

![[Pasted image 20230827130011.png]]

### Benefits of Multithreading

* Parallelization => Speed UP
* Specialization => Hot Cache!
* Efficiency => lower memory management requirement& cheaper IPC

### Benefits of Multithreading: # Threads > # CPUs

![[Pasted image 20230827171717.png]]

* if (t_idle)>2*(t_ctx_switch) then context switch to hide idling time
* t_ctx_switch threads < t_ctx_switch processes
	* because threads are in a shared address space even in a single CPU
* hide latency

### Benefits of Multithreading: Apps and OS

![[Pasted image 20230827172036.png]]

### Basic Thread Mechanisms

* What we need to support thread?
	* thread data structure
		* identify threads, keep track of resources
	* mechanisms to create and manage threads
	* mechanisms to safely coordinate among threads running concurrently in the same address space
* Concurrency Control & Coordination![[Pasted image 20230827201858.png]]
	* mutual exclusion
		* exclusive access to only one thread at a time
		* mutex
	* wait on other threads
		* specific condition before proceeding
	* waking up other threads from the wait stage

### Thread Creation

* Thread type
	* thread data structure ![[Pasted image 20230827202600.png]]
* Fork (proc, args)
	* create a thread
	* not UNIX fork
* Join (thread)
	* terminate a thread
* ![[Pasted image 20230827203156.png]]

### Mutual Exclusion

* Mutex
	* It is like a Lock![[Pasted image 20230827204823.png]]
	* Critical Section: The portion of code protected by the Mutex
	* ![[Pasted image 20230827205302.png]]

### Condition Variable

![[Pasted image 20230827213108.png]]

* use the Signal to notify wait function for consumer to modify the list when it is full

### Condition Variable API

* Condition type data structure
* Wait (mutex, cond)
	* mutex is automatically released and re-acquired on wait
* Signal (cond)
	* notify only one thread waiting on condition
* Broadcast (cond)
	* notify all waiting thread
* Why we use while instead of i ![[Pasted image 20230827213837.png]]

### Reader/Writer Problem

* Problem Description  
![[Pasted image 20230827215254.png]]

* Example Code![[Pasted image 20230828210205.png]]![[Pasted image 20230828210632.png]]
* General Structure![[Pasted image 20230828210229.png]]
* Conceptual Critical Section![[Pasted image 20230828210618.png]]
* Critical Section Structure with Proxy Variable![[Pasted image 20230828210900.png]]
	* By pass the limitation of mutex so that we can perform more complicated operation

### Common Pitfalls

* keep track of mutex / cond. variables used with a resource
	* e.g., mutex_type
* check that you are always (and correctly) using lock & unlock
	* e.g., did you forget to lock / unlock? what about compilers?
* use a single mutex to access a single resources!
* check that you are signaling correct condition
* check that you are not using signal when broadcast is needed
	* signal: only 1 thread will proceed … remaining threads will continue to wait … possibly indefinitely
* ask yourself: do you need priority guarantees?
	* thread execution order not controlled by signals to condition variables
* spurious wake ups![[Pasted image 20230828212126.png]]
	* when we wake threads up knowing they may not be able to proceed
	* can we unlock the mutex before broadcast / signal?![[Pasted image 20230828212344.png]]
	* We can do it on writer but not reader![[Pasted image 20230828212450.png]]
* dead locks
* ![[Pasted image 20230828213103.png]]
	* **definition**
		* two or more competing threads are waiting on each other to complete, but none of them ever do
	* **how to avoid**
		* unlock A before locking B
			* but threads need both A&B
		* get all locks upfront, then release at the end
		* use on mega lock
			* can work but too restrictive => limits parallelism
		* maintain lock order![[Pasted image 20230828213525.png]]
			* first m_a
			* then m_b
			* can prevent cycles in wait graph
	* **summary**
		* a cycle in the wait graph is necessary and sufficient for a deadlock to occur
		* deadlock prevention (expensive)
		* deadlock detection & recovery (rollback)
		* apply the ostrich algorithm => do nothing!
		* if all else fails just reboot

### Kernel vs. User-level Threads

* Multithreading Models
	* One to One Model![[Pasted image 20230828215257.png]]
	* Many to One Model![[Pasted image 20230828215518.png]]
	* Many to Many Model![[Pasted image 20230828215745.png]]
* Scope of Multithreading
	* system scope
		* system-wide thread management by OS-level thread managers (e.g. CPU scheduler)
		* it will scheduled threads based on resources requirements
	* process scope
		* user-level library manages threads within a single process
		* it will scheduled threads based on the OS's perspective on process because it has no visibility on their resources requirements
* Multithreading patterns
	* Boss/Workers Pattern
		* boss: assigns work to workers
		* worker: performs entier task
		* throughput
			* throughput of the system limited by boss thread => must keep boss efficient
			* throughput = 1/(boss_time_per_order)
		* boss assigns work by:
			* directly signaling specific worker
				* * workers don't need to synchronize
				* boss must track what each worker is doing
				* throughput will go down
			* placing work in producer / consumer queue
				* * boss doesn't need to know details about workers
				* queue synchronization
		* how many workers:
			* on demand
			* pool of workers created upfront
				* static v.s. dynamic
		* pros and cons:
			* * simplicity
			* thread pool management
			* locality
	* Boss-Worker Variants![[Pasted image 20230828221703.png]]
	* Pipeline Pattern![[Pasted image 20230828222358.png]]
		* threads assigned one subtask in the system
		* entire tasks == pipeline of threads
		* multiple tasks concurrently in the system, in different pipeline stages
		* throughput == weakest link
			* pipeline stage == thread pool
		* shared-buffer based or communication b/w stages
	* Layered Pattern![[Pasted image 20230828222615.png]]
	* Time Calculation![[Pasted image 20230828223812.png]]
