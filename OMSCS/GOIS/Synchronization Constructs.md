# Visual Metaphor

- Synchronization is like waiting for a coworker to finish so you can continue working
    - may repeatedly check (sync using spinlocks)
    - may wait for signal (sync using mutexes and condition variables)
    - waiting hurt performance (CPU waste, cycle for checking, cache effects)

# More about Synchronization

- Limitation of mutexes and condition variables
    - error prone / correctness / ease-of-use
        - unlock wrong mutex, signal wrong condition variable
    - lack of expressive power
        - helper variable for access or priority control
- Low level Support
    - hardware atomic instructions

# Spinlocks

- similar to mutex
    - mutual exclusion
    - lock and unlock(free)
- but
    - lock == busy
        - ⇒ spinning, it will use the CPU

# Semaphores

- common sync construct in OS kernels
- like a traffic light: STOP and GO
- similar to a mutex but more general
- on init
    - assigned a max value (positive init)⇒ maximum count
- on try (wait)
    - if non-zero⇒ decrement and proceed ⇒ counting semaphore
- if initialized with 1
    - semaphore == mutex(binary semaphore)
- on exit(post)
    - increment

# Reader Writer Locks

- read(never modify) == shared access
- write(always modify) == exclusive access

# Using Reader Writer Locks

- Semantic differences
    - recursive read lock ⇒ read-unlock?
    - upgrade / downgrade priority?
    - interaction with scheduling policy
        - e.g., block if higher priority writer waiting

# Monitors

- Monitors specify
    - shared resources
    - entry procedure
    - possible condition variables
- On entry
    - lock, check
- On exit
    - unlock, check, signal
- Monitors == high-level synchronization construct
    - MESA by XEROX PARC
    - Java
        - synchronized methods generate monitor code
        - notify() explicitly
- Monitors == programming style
    - enter / exit critical section in Threads and Currency

# More Synchronization Construct

- serializes
- path expressions
- barriers
- rendezvous points
- optimistic wait-free sync (RCU)
- All need hardware support!

# Atomic Instructions
- Hardware-specific
	- test_and_set
	- read_and_increment
	- compare_and_swap
- Guarantees
	- atomicity
	- mutual exclusion
	- queue all concurrent instructions but one
- atomic instructions
	- critical section with hardware-supported synchronization
-  ![[Pasted image 20231031221419.png]]

# Shared Memory Multiprocessors
![[Pasted image 20231031221830.png]]
![[Pasted image 20231031222214.png]]
# Cache Coherence
- non-cache-coherent (NCC) vs. coherent (CC)
- can achieve cache coherent via hardware support
- ![[Pasted image 20231031225226.png]]\\
# Cache Coherence and Atomics
![[Pasted image 20231031225708.png]]
# Spinlock Performance Metrics
![[Pasted image 20231031225944.png]]
# Test and Set Spinlock
![[Pasted image 20231031230514.png]]
# Test and Test and Set Spinlock
![[Pasted image 20231031231209.png]]
# Spinlock Delay Alternatives
![[Pasted image 20231031231929.png]]
![[Pasted image 20231031232027.png]]
# Picking a Delay
- Static Delay
	- simple approach
	- unnecessary delay under low contention
- Dynamic Delay
	- random delay in a range that increases with "preceived" contention
	- preceived == failed test_and_set()
	- delay after each reference will keep growing based on contention or length of critical section
# Queueing Lock
- Common problem in spinlock implementation
	- Everyone tries to acquire a lock at the same time once lock is freed
		- delay alternatives
	- Everyone sees the lock is free at the same time
		- Anderson's Queueing lock
	- ![[Pasted image 20231031233040.png]]
# Queueing Lock Implementation
![[Pasted image 20231031233532.png]]
