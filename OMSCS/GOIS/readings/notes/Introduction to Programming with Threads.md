# Introduction
- Programming with threads introduces new difficulties
- Thread is A single sequential flow of control
- Multiple threads: 
	- At any instant the program has multiple points of execution, one in each of its threads
	- threads as executing simultaneously
- "single address space": permit the threads to read and write the same memory locations
- each thread executes on a separate call stack with its own separate local variables
- 