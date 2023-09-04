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

# Thread Data Structures: At Scale
- 
