# Visual Metaphor
![[Pasted image 20231011173959.png]]
# Memory Management: Goals
- Virtual vs. Physical memory
- ![[Pasted image 20231011195417.png]]
	- Allocate
		- allocation, replacement...
	- Arbitrate
		- address translation and validation
- Page-based memory management
	- Allocate =>pages (fixed size segment) - > page frames (fixed size)
	- Arbitrate => page tables
- Segment-based memory management
	- Allocate: segments
	- Arbitrate: segment registers
# Memory Management: Hardware Support
- ![[Pasted image 20231011200951.png]]
- CPU issues virtual memory addresses
- MMU (memory management unit)
	- translate virtual to physical addresses
	- reports faults: illegal access, permission, not present in memory
- Registers
	- pointers to page table
	- base and limit size, number of segments
- Cache - Translation Lookaside Buffer
	- valid VA-PA translations: TLB
	- make it faster
- Translation
	- actual PA generation done in hardware
# Page Tables
![[Pasted image 20231011202442.png]]
- virtual memory pages and physical memory pages frames are the same size
- virtual page number (VPN) + offset = Physical Frame Number(PFN)
-  Allocation on first touch
	- init_array(&array_addr) => create a array address in virtual space
	- take a physical address and establish a mapping in page table if this array is not accessed before
- unused pages == reclaimed
	- if the physical address is not used for a long time
	- in page table , we have a valid bit column to indicate if page is valid or not
	- mapping invalid => hardware will fault => OS handling this (trap handling)
	- reestablish on re-access (might be new address)
- page table summary
	- per process
	- switch to valid page table on context switch
		- update register (pointer to the page table)
# Page Table Entry
- Page Frame Number
- Flags
	- Persent (valid / invalid)
	- Dirty (written to)
	- Accessed (for read or write)
	- protection bits => RWX
- Page table entry on x86
	- ![[Pasted image 20231011215040.png]]
- Page Fault
	- generate error code on kernel stack => trap into kernel
	- page fault handler
		- determines action based on error code and faulting address
			- bring page from disk to memory
			- protection error(SIGSEGV)
		- on x86
			- error code from PTE(page table entry) flags
			- faulting address in register CR2
# Page Table Size
- 32-bit architecture
	- Page Table Entry(PTE)
		- 4 bytes, including PFN + Flags
	- Virtual Page Number(VPN)
		- 2^23 / page size
	- Page Size
		- 4kb (..8kb,...)
		- (2^32/2^12) x 4B = 4MB => per process 
- process doesn't use entire address space
- even on 32-bit arch will not always use all of 4GB
- But page table assumes an entry per VPN, regardless of whether corresponding virtual memory is needed or not
# Multi Level Page Tables
- Hierarchical Page Tables
	- ![[Pasted image 20231011220314.png]]
	- outer page table or top page table == page table directory
	- internal page table == only for valid virtual memory regions
	- malloc might create new page of page table
	- Address Split
		- ![[Pasted image 20231011220441.png]]
		- 2^10 x page size = 2^10 x 2^10 = 1MB
		- don't need an inner table for each 1MB virtual memory gap
	- Additional Layer
		- page table directory pointer (3rd level)
		- page table directory pointer map (4th level)
		- important on 64bit architectures
		- larger and more sparse
			- larger gaps => could save more internal page table components
	- Multi-level PT tradeoffs
		- + smaller internal page tables / directories; granularity of coverage => reduced page table size
		- - more memory accesses required for translation => increase translation latency
		- Quiz![[Pasted image 20231011223824.png]]
			- Format 1
				- 2^6 = 64
			- Format 2
				- 2^(4+6) = 1 KB
				- outer table has 2 bits so 4 combinations, each one will contain 1KB virtual address 
				- we only use 3 KB in total
				- 3 x 2^4 = 48
# Speeding Up Translation TLB
## Overhead of Address Translation
![[Pasted image 20231012190539.png]]
## Page Table Cache (TLB)
![[Pasted image 20231012190725.png]]
# Inverted Page Tables
![[Pasted image 20231012192106.png]]
- build it based on physical memory elements
- slow linear search, PLB to the recuse
- Hashing Page Tables
	- hash function to has table
	- point to a linked list of possible search
	- speed up the linear search
# Segmentation
![[Pasted image 20231012203014.png]]
- segments == arbitrary granularity
	- e.g., code, heap, data, stack ...
	- addr == segment selector + offset
- segment == contiguous physical memory
	- segment size == segment + base + limit registers
- Segmentation + Paging
	- IA x86_32 => segmentation + paging
		- Linux: up to 8k per process / global segment
	- IA x86_64 => paging
# Page Size
![[Pasted image 20231012203812.png]]
# Memory Allocation
- memory allocator
	- determines VA to PA mapping
	- address translation, page tables
		- simply determine PA from VA and check validity / permissions
- kernel-level allocators
	- kernel state, static process state
- user-level allocators
	-  dynamic process state (heap), malloc / free
	- e.g., dlmalloc, memalloc, hoard, tcmalloc
# Memory Allocation Challenges
