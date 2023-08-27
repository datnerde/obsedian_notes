# Simple Process Definition
* Instance of an executing program
* Synonymous with task or job
# Metaphor
> [!quote]  
> An process  is like a an order of toys

- State of execution
	- program counter, stack
- Parts & temporary holding area
	- data, register state occupies state in memory
- May require special hardware
	- I/O devices
# What is a Process?
* OS manages hardware on behalf of applications (program on disk, flash memory as static entity)
* Process: state of a program when executing loaded in memory (active entity)
# What Does a Process Look Like?
* Types of state
	* Text and Data
		* Static state when process first loads
	* Heap
		* dynamically created during execution
	* Stack
		* grows and shrinks ~ LIFO queue
# Process Address Space
> [!tip]  
> Decouple virtual address from physical address for the process
* Address space
	*  'in memory'  representation of a process
* Page tables
	* mapping of virtual to physical addresses
# Address Space and Memory Management
* parts of virtual address space may not be allocated
* may not be enough physical memory for all state
* portions of project 1 / project 2 may be allocated in DRAM and Disk, depending on the need to save space![[Pasted image 20230826185853.png]]
# Process Execution State
* How does the OS know what a process is doing? 
	* A series of trackers for the OS to know where are we
		* Program Counter
		* CPU registers
		* Stack Pointer
# Process Control Block
![[Pasted image 20230826191447.png]]
> [!quote]  
> Data Structure that the OS maintains for every one of the processes that it manages

* PCB created when process is created
* Certain fields are updated when process state changes
* Other fields change too frequently
# How is a PCB Used?
* OS will save information to PCB when the project is interrupted (kind of like a bookmark for resuming the work in the future)
# Context Switch
* switching the CPU from the context of one process to the context of another
* they are expensive
	* direct costs: number of cycles for load & store instructions
	* indirect costs: COLD cache / cache misses
# Process Life Cycle: States
![[Pasted image 20230826194922.png]]
* Ready and running state can be executed by CPU
# Process Life Cycle: Creation
- Mechanisms for process creation
	- fork = copies the parent PCB into new child PCB
	- exec = child contin