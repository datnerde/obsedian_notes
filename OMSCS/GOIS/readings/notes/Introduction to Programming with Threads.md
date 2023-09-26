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
	- When a procedure returns, the thread dies
	- The fork returns a caller handle which is sometimes joined (i.e., join means the calling thread waits for the thread to die before continuing)
	```
	TYPE Thread; 
	TYPE Forkee = PROCEDURE(REFANY): REFANY;
	PROCEDURE Fork(proc: Forkee; arg: REFANY): Thread; 
	PROCEDURE Join(thread: Thread): REFANY;
	```
- Mutual exclusion
	- avoid errors arising when more than one thread is accessing the shared variables
	- a primitive that offers mutual exclusion, specifying for a particular region of code that only one thread can execute there at any time
	```
	TYPE Mutex;
	LOCK mutex DO ... statements ... END ;
	```
	- A mutex has two states
		- locked and unlocked
		- initially unlocked
	- achieve mutual exclusion
		- associating them with a mutex
		- accessing the variables only from a thread that holds the mutex
- Condition variables
	- a mechanism that allows a thread to block until some event happens
	```
	 TYPE Condition; 
	 PROCEDURE Wait(m: Mutex; c: Condition); 
	 PROCEDURE Signal(c: Condition); 
	 PROCEDURE Broadcast(c: Condition);
	```
	- always associated with a particular mutex
	- 'wait' unlocks the mutex and blocks the thread
		- if a thread is awoken inside 'wait' after blocking, it re-locks the mutex then returns
	- 'signal' awakens at least one such blocked thread
	- 'broadcast' awakens all threads blocked
- Alerts
	- A mechanism for interrupting a particular thread
	- 'alert-pending' = False initially
	- 'alertwait' similar to 'wait', except that it will 
		- sets alert-pending = False
		- re-locks m and raises the exception 'alerted'
	- 'testalert' tests and clears the alert-pending boolean
# Using a mutex: Accessing shared data
- Unprotected data
	- 