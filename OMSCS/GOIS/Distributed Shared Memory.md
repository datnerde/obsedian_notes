![[Pasted image 20231113195605.png]]
# Peer Distributed Applications
![[Pasted image 20231113201343.png]]
# Distributed Shared Memory (DSM)
- Each node
	- "owns" state => memory
	- provides service
		- memory reads / writes from any node
		- consistency protocols
- permits scaling beyond single machine memory limits
	- more "shared" memory at lower cost
	- slower overall memory access
	- commodity interconnect technologies support this (RDMA)
# Hardware vs Software DSM