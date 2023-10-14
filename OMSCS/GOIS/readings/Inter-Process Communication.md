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
	- 