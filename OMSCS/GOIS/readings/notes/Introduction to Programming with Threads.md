## Introduction

- Programming with threads introduces new difficulties
- Thread is A single sequential flow of control
- Multiple threads:
	- At any instant the program has multiple points of execution, one in each of its threads
	- threads as executing simultaneously
- "single address space": permit the threads to read and write the same memory locations
- each thread executes on a separate call stack with its own separate local variables
- The programmer has to synchronize the threads to the shared (global memory)
----

## Why Use Concurrency

- The advent of multi-processeors
- Useful in driving slow devices such as disks, networks, terminals and printers
- Human users want their computer to do multiple works
- Building a distributed system needs concurrency to handle clients' requests in parallel
----

## The Design of a Thread Facility

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

## Using a Mutex: Accessing Shared Data

- All shared mutable data must be protected by associating it with some mutex
- And you must access the data only from a thread that is holding the mutex
- Unprotected data
	- Fail to protect some mutable data and then you access it wo the benefits of synchronization
	- the effects of unsynchronized access is non-deterministic
- Invariants
	- a boolean function of the data that is true whenever the mutex is not held
	- each thread has the responsibility to restore the invariant before releasing the mutex
- Cheating
	- skip mutex because of the simplicity in code and machine
- Deadlocks involving only mutexes
	- apply a partial order to the acquisition of mutexes (e.g., make sure M1 is always locked before M2)
	- Breakdown your mutexes into smaller chunk
- Poor performance through lock conflicts
	- to get good performance, you must arrange that lock conflicts are rare events
	- lock at a finer granularity ; but this introduces complexity
- Releasing the mutex within a LOCK clause
	- "acquire" and "release" because you want to avoid blocking the thread for a long time due to long-time execution
	- vicinity of forking: transfer the holding of the mutex to the newly forked thread
	- don't recommend to do this

## Using a Condition Variable: Scheduling Shared Resources

- WHILE NOT expression DO Thread.Wait(m,c) END;
- re-testing the condition
	- "signal" dose not guarantee that the awoken thread will be the next to lock the mutex
	- SRC "signal" may wake up more than one thread
	- make your program more obviously, robust and correct
	- it allows for simple programming of calls to "Signal" or "Broadcast"
- Using "Broadcast"
	- The correctness of the program will be unaffected between "signal" / "broadcast" after applying the re-checking style
	- One use of "Broadcast" trades poorer performance for greater simplicity
	- shared / exclusive locking
- Spurious wake-ups
	- awakening threads that cannot make useful progress
	- you should probably separate the blocked threads onto two conditions variables
		- one for readers
		- and one for writers
- Spurious lock conflicts
	- excessive scheduling overhead
		- a terminating reader calls "signal" and still has the mutex locked
			- the writer will be awakened
			- the write will continue to work when reader unlocks the mutex (two extra re-scehdule operations)
		- we can move the signal after the lock clause
	- a terminating writer calls "broadcast"
		- only one reader can lock the mutex, but other readers are also trying to lock the mutex causing the block
		- we can awaken just one reader and having each reader in turn awaken the next
- Starvation
	- when some thread will never make progress.
		- here is always at least one thread wanting to be a reader, but the system is heavily loaded.
		- the writer can never proceed
		- we can add a counter for blocked writers, and defer the reader
- Complexity
	- whether the potential cost of ignoring the problem is enough to merit writing a more complex program
- Deadlock
	- avoid by assigning order on the resources managed by the condition variables
	- lock a mutex at one abstraction level of your program then call down to a lower level, which blocks
		- explicitly unlock the mutex before calling the lower level abstraction

## Using Fork: Working in Parallel

- Reasons to fork a thread
	- utilize multiple processors
	- do work while waiting for I/O
	- Satisfy multitasking humans
	- provide a network service to multiple clients
	- defer work until a less busy time
- Applications use several threads, for example:
	- Computation thread
	- Writing output to file thread
	- User input thread
	- Background thread to clean up data structures
- If you don't want to wait for a device, create a thread
- If you want multiple device request, use multiple threads
- If you are interacting with a user, you'll want a separate thread to deal with and respond
- Network servers will require separate threads
	- RPC protocol requires separate threads already
	- If you are writing a client program, create a separate thread to contact the server
- Strategies
	- Once a procedure has a usable result, fork the thread and complete the rest of the work and return to the original thread
		- However this could create large numbers of threads and forking has a time cost
	- Instead, keep a single housekeeping thread and feed requests to it
		- Also, the housekeeper can merge similar requests and only run after a certain period of time
- Pipelining
	- A chain of producer-consumer relationship
	- be careful about how much of the work gets done in each stage (hopefully each stage workload is equal)
	- number of stages determines statically the amount of concurrency
- The impact of your environment
	- design of OS and runtime libraries will affect the extent to which it is desirable to fork threads
		- should not suspend the entire address space just because on thread is blocked on i/o
		- should be available as synchronous calls that block only calling thread
	- cost of a thread / cost of keeping a blocked thread in existence / context switch
- Potential problems with adding threads
	- performance degrades if ***ready to run*** threads >> processors
		- thread schedulers are slow at re-scheduling decision
		- conflicts over mutexes or over the resources managed by condition variables
	- cost of thread creation and termination are not cheap
		- smallest computation for which it is profitable to fork a thread (measurement of thread implementation)

## Using Alert: Diverting the Flow of Control

- purpose
	- termination of along running computation or a long-term wait
- any procedure in a public interface that might incur a long computation or a long-term wait should be alertable
- only alert a thread if you forked the thread
- using them will tend to make your program less well structured
- alters are most useful when you don't know exactly what is going on

## Additional Techniques

- Up-calls
	- calling a higher level abstraction
		- no unnecessary context switches
		- programmer's task has been made more complicated: up-call & down-call
		- more likely to violate the partial order rule for locking mutexes
			- avoid holding a mutex while making an up-call
- Version stamps
	- avoid cache issues
		- maintain a counter associated with the true data in a lower level
		- higher level also caches the associated counter value
		- low level receives and compares the counter value and return an exception to high level to re-consider its call
	- also useful in distributed system
- Work crews
	- when you have more concurrency than can be run on your hardware
	- be more retrained on forking / abstraction that control forking
		- fixed pool of threads that perform the requests
	- defers fork until there is a processor available to run it => lazy forking

## Building Your Program

- design interfaces with the assumption that your callers will be using multiple threads
- "Correct" means your program produces and answer according to a specification
- "Live" means your program will eventually produce an answer
- "Efficient" means the program makes good use of the available resources and produces its answer quickly
