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
- page-based DSM architecture
	- distributed nodes, each w/own local mm contribution
	- pool of pages from all nodes
	- each page has ID, page frame number
- if MRMW
	- need local caches for performance (latency)
	- home (or manager) node drives coherence ops
	- all nodes responsible for part of distributed memory (state) management
- "Home" node
	- keep state: pages accessed, modifications, caching enabled /disabled, locked...
	- current "owner" (owner may not equal home node)
- Explicit replicas
	- for load balancing, performance, or reliability
	- "home" / manager node controls management
- summary
![[Pasted image 20231113221242.png]]
# Summarizing DSM Architecture
![[Pasted image 20231113221344.png]]
# Indexing Distributed State
- DSM Metadata
	- Each page (object) has...
		- address == node ID + page frame number
		- node ID == "home" node
	- Global map (replicated)
		- object(page) id => manager node id
		- manager map available on each node!
	- Metadata for local pages (partitioned)
		- per. page metadata is distributed across managers
	- Global mapping table
		- object id => index into mapping table => manager node
![[Pasted image 20231113221955.png]]
# Implementing DSM
- Problem: DSM must "intercept" accesses to DSM state
	- to send remote messages requesting access
	- to trigger coherence messages
	- => overheads should be avoided for local, non-shared state (pages)
	- => dynamically "engage" and "disengage" DSM when necessary
- Solution: Use hardware MMU support!
	- trap in OS if mapping invalid or access not permitted
	- remote address mapping => trap and pass to DSM to send msg
	- cached content => trap and pass to DSM to perform necessary coherence ops.
	- other MMU information useful (e.g., dirty page)
- 