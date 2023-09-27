# Abstract
----
* Using threads makes the kernel fully preemptible and capable of real-time response
# Introduction
----
- support multiprocessors in SunOS; go further than just adding locks
- support more than one thread of control within a user process
- capable of low latency / user-level multithreading
# Overview of the Kernel Architecture
----
- Kernel Threads are lightweight
	- small data structure and stack
	- switching does not require changing virtual memory address
	- fully preemptible
- Kernel Threads are used to:
	- provide asynchronous kernel activity
		- remove diversions in the idle loop and trap code
		- replaces them with independently scheduled threads
	- interrupts are also handled by kernel threads
	- support of multiple kernel-supported threads of control 
		- LWPs = lightweight processes
		- while all LWPs have a kernel thread, not all kernel threads have an LWP
	- user-level library
		- uses LWPs to implement user-level threads
		- scheduled at user-level and switched by the library to any of the LWPs belonging to the process
		- bound to a particular LWP
		- user-level threads can be switched between without entering the kernel
	- 