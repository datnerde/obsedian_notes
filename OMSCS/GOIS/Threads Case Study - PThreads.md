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