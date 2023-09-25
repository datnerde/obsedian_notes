# Introduction
- Programming with threads introduces new difficulties
- Thread is A single sequential flow of control
- Multiple threads: 
	- At any instant the program has multiple points of execution, one in each of its threads
	- threads as executing simultaneously
- "single address space": permit the threads to read and write the same memory locations
- each thread executes on a separate call stack with its own separate local variables
- The programmer has to synchronize the threads to the shared (global memory)
----
# Why use concurrency
- The advent of multi-processeors
- Useful in driving slow devices such as disks, networks, terminals and printers
- Human users want their computer to do multiple works
- Building a distributed system needs concurrency to handle clients' requests in parallel
----
# The design of a thread facility
- Thread creation
	- using "Fork" to create a new thread
	- using "Join" to wait for a given thread to terminate
- Mutual exclusion
- Waiting for events
- 