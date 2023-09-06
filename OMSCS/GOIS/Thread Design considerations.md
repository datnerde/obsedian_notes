# Preview
- Kernel vs. user-level threads
- Threads and interrupts
- Threads and signal handling

# Kernel vs. User Level Threads
![[Pasted image 20230904160322.png]]
# Thread Data Structures: Single CPU
![[Pasted image 20230904161801.png]]
- For multi-thread cases
	- we breaks the info in PCB into KLT for each thread
	- The PCB will still contain info of virtual address mapping for the whole process warped in user level
	- Thread_lib will contain info for each user-level thread (ULT)

# Thread Data Structures: At Scale![[Pasted image 20230904162643.png]]
# Hard and Light Process State
![[Pasted image 20230904195922.png]]
- split information originally in PCB
	- hard process state contains all user-level threads that execute within that process
	- light process state contains user-level threads that are associated with kernel level threads
# Rationale for Data Structures
- Single PCB
	- characteristics
		- large continuous data structure
		- private for each entity
		- saved and restored on each context switch
		- update for any changes
	- cons
		- scalability
		- overheads
		- performance
		- flexibility
- Multiple data structures
	- characteristics
		- smaller data structures
		- easier to share
		- on context switch only save and restore what needs to change
		- user-level library need only update portion of the state
	- pros
		- scalability
		- overheads
		- performance
		- flexibility
# User Level Structures in Solaris 2.0
![[Pasted image 20230905203950.png]]
- LWP == Light Weight Process
- CPU == Central Processing Unit
- Implementing lightweight threads by Stein & Shah
	- not POSIX threads, but similar
	- thread creation => thread ID(tid)
		- tid => index into table of pointers
		- table pointers point to per thread data structure
	- stack growth can be dangerous
		- solution => red zone![[Pasted image 20230905204503.png]]
# Kernel Level Structures in Solaris 2.0
- process
	- list of kernel-level threads
	- virtual address space
	- user credentials
	- signal handlers
- light-weight process (LWP)
	- user- level registers
	- system call args
	- resource usage info
	- signal mask
	- similar to ULT, but visible to kernel to kernel 
	- not needed when process not running