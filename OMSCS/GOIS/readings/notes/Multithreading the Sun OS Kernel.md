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
		- allows a user process to have thousands of threads without overwhelming kernel resources
# Data Structures
---
- Traditionally, `user` and `proc` structures contained all kernal data for a given process
- The new kernel separated the data into data associated with each LWP and its kernel thread
- Per-process data is contained in the `proc` structure and contains a list of:
    - kernel threads associated with the process
    - pointer to the process address space
    - user credentials
    - list of signal handlers
- The LWP structure contains:
    - PCB (Process Control Block)
        - processor registers
        - system call arguments
        - signal handling masks
        - resource usage info
        - profiling pointers
    - Pointers to the kernel thread and process structures
- The Kernel Thread structure contains:
    - kernel registers
    - scheduling class
    - dispatch queue links
    - pointers to the stack and associated LWP, process, and CPU structures
- Per-processor data is kept in the `cpu` structure
    - contains pointers to the currently executing thread, idle thread, dispatching and interrupt handling information
- To speed access to the thread, LWP, process, and CPU structures, there is a global register (%g7) that points to the current thread structure
# Kernel Thread Scheduling
-----
- A scheduling class determines the relative priority of processes within a class and converts it to a global priority
    - The scheduling class and dispatcher operate on threads instead of processes
    - Three Scheduling classes in SPARC
        - system
        - time-share
        - real-time (Fixed Priority)
- The dispatcher choose the thread with the greatest global priority
    - If there are two with the same priority, they are dispatched in round robin order
- By making the kernel preemptible, the real-time class and interrupt threads are better supported
# System Threads
---
- Can be created for short and long term activities
- Scheduled like any thread but belong to system scheduling class
- No need for LWP structure so the thread and stack are allocated together in a non-swappable area
- The segment driver, `seg_kp` handles stack allocations
    - Also handles virtual memory allocations for the kernel and provides "red zones" to protect stack overflows
# Synchronization Architecture
---
