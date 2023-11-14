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
![[Pasted image 20231113210811.png]]
# DSM Design: Sharing Granularity
- cache line granularity
	- => overheads too high for DSM
- variable granularity (still too find granularity, and overheads)
- page granularity (OS-level)
- object granularity (language runtime)
- => beware of false sharing
	- e.g., X and Y are on same page
# DSM Design: Access Algorithm
- single reader / single writer (SRSW)
- multiple readers / single writer (MRSW)
- multiple readers / multiple writers (MRMW)
# DSM Design: Migration vs Replication
![[Pasted image 20231113214742.png]]
# DMS Design: Consistency Management
- Recap consistency management in Shared memory processors
![[Pasted image 20231113215245.png]]
- Push invalidations when data is written to
	- proactive
	- eager
	- pessimistic
- Pull modification info periodically
	- on-demand (reactive)
	- lazy
	- optimistic
- => when these methods get triggered depends o the consistency model for the shared state
# DSM Architecture
