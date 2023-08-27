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
* Address space
	*  'in memory'  representation of a process
* Page tables
	* mapping of virtual to physical addresses