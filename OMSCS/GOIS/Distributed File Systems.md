# DFS Visual Metaphor
![[Pasted image 20231113173850.png]]
# DFS
- multiple machine involved the delivery of file system service forms DFS
# DFS Models
![[Pasted image 20231113174626.png]]
# Remote File Service: Extremes
![[Pasted image 20231113174756.png]]
![[Pasted image 20231113174928.png]]
# Remote File Service: A Compromise
![[Pasted image 20231113175304.png]]

# Stateless vs. Stateful File Server
![[Pasted image 20231113175856.png]]
# Caching State in a DFS
- locally clients maintain portion of state (e.g., file blcoks)
- locally clients perform operations on cached state(e.g., open/read/write...)
- => requires coherence mechanisms
![[Pasted image 20231113180216.png]]
- where files or file blocks can be cached in a DFS with a single file server and many clients
	- in client memory
	- on client storage device (HDD/SSD)
	- in buffer cache in memory on server (usefulness will depend on clients load / request interleaving...)
# File Sharing Semantics on a DFS
 - UNIX semantics => every write visible immediately
 - Session semantics (between open-close => session)
	 - write-back on close(), update on open()
	 - easy to reason, but may be insufficient
 - Periodic Updates
	 - client writes-back periodically => clients have a "lease" on cached data (not exclusive necessarily)
	 - server invalidates periodically => provides bounds on "inconsistency"
	 - augment with flush()/sync() API
 - Immutable files => never modify, new files created
 - Transactions => all changes atomic