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
