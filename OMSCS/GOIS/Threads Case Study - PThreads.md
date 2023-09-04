# Overview
* PThreads == POSIX Threads
* POSIX == Portable OPperating System Interface
* POSIX Threads
	* POXIS versions of Birrell's API
	* specifies syntax and semantics of the operations
# PThread Creation
![[Pasted image 20230902181948.png]]
- PThread Attributes
	- pthread_attr_t
		- specified in pthread_create
		- defines features of the new thread
		- has default behavior with NULL in pthread_create
		- ![[Pasted image 20230904141512.png]]
	- Detaching Pthreads![[Pasted image 20230904141641.png]]
		- to detach a thread![[Pasted image 20230904142127.png]]
		- to create a detached thread![[Pasted image 20230904142152.png]]
		- the detached thread can exit ![[Pasted image 20230904142221.png]]
# Compiling PThreads
![[Pasted image 20230904142550.png]]
# Code Example
![[Pasted image 20230904143711.png]]
- the above mentioned will happen due to data race or race condition
	- a thread tries to read a value, while another thread modifies it
- How to avoid the problem![[Pasted image 20230904143807.png]]
# Pthread Mutexes
>[!quote]
>to solve mutual exclusion problems among concurrent threads
- Pthreads implementation
	- Lock and Unlock
		- ![[Pasted image 20230904144044.png]]
		- ![[Pasted image 20230904144200.png]]
	- Other Mutex Operations
		- initialize mutex (null attribute is default)![[Pasted image 20230904144506.png]]
		- try lock and destroy![[Pasted image 20230904144622.png]]
- Mutex Safety Tips
	- shared data should always be accessed through a single mutex!
	- mutex scope must be visible to all!
	- globally order locks
		- for all threads, lock mutexes in order
	- always unlock a mutex
		- unlock the correct mutex
# Tthread Condition Variables
- PThread Implementation![[Pasted image 20230904144918.png]]
- Other Operation
	- initialization condition variable![[Pasted image 20230904144955.png]]
	- destroy condition variable![[Pasted image 20230904145007.png]]
- Tips
	- Do not forget to notify waiting threads!
		- predicate change
			- signal / broadcast correct condition variable
	- when in doubt broadcast
		- but performance loss
	- you do not need a mutex to signal / broadcast