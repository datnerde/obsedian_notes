# Visual Metaphor
![[Pasted image 20231013180542.png]]
# Inter Process Communication
- OS-supported mechanisms for interaction among processes (coordination & communication)
	- message passing
		- e.g., sockets, pipes, message queues
	- memory-based IPC
		- shared memory, memory mapped files ..
	- high-level semantics
		- files, RPC
	- synchronization primitives
# Message Based IPC
![[Pasted image 20231014130612.png]]
- send/recv of messages
- OS creates and maintains a channel
	- buffer, FIFO queue...
- OS provides interface to processes - a port
	- processes send/write messages to a port
	- processes recv/read messages from a port
- kernel required to
	- establish communication
	- perform each IPC op
		- send: system call + data copy
		- recv: system call + data copy
-  request-response:
	- 4x user/kernel crossings + 4x data copies
- - overheads
- + simplicity:
	- kernel does channel management and synchronization
# Forms of Message Passing
- Pipies
	- carry byte stream between 2 processes
	- e.g., connect output from on process to input of another
- Message Queues
	- carry "messages" among processes
	- OS management includes 
		- priorities
			- scheduling of msg delivery
	- APIs: sysV and POSIX
- Sockets
	- send(), recv() == pass message buffers
	- socket() == create kernel-level socket buffer
	- associate necessary kernel-level processing (TCP/IP,...)
	- if different machines, channel b/w process and network device
	- if same machine, bypass full protocol stack
# Shared Memory IPC
![[Pasted image 20231014131351.png]]
- read and write to shared memory region
	- OS established shared channel b/w the processes
		- physical pages mapped into virtual address space
		- VA(P1) and VA(P2) map to the same physical address
		- VA(P1) not need to be equal VA(P2)
		- physical memory doesn't need to be contiguous
- + system calls only for setup (because only in user scope after setup)
- + data copies potentially reduced (but not eliminated)
- - explicit synchronization
- - communication protocol
- - shared buffer management
- APIs: Sys V API, POSIX API, memory mapped files, Android ashmen
# Copy vs. Map
![[Pasted image 20231014132246.png]]
# SysV Shared Memory
- "segments" of shared memory => not necessarily contiguous physical pages
- shared memory is system-wide => system limits on number of segments and total size
- Create
	- OS assigns unique key
- Attach
	- map virtual => physical addresses
- Detach
	- invalidate address mappings
- Destroy
	- only remove when explicitly deleted (or reboot)
# SysV Shared Memory API
 ![[Pasted image 20231014134139.png]]
# POSIX Shared Memory API
 