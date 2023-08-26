## Simple OS Definition

- A special software that
	- Abstracts and : Simplify what hardwares actually look like
	- Arbitrates: To manage, control & oversee the hardware
	- The use of a computer system

## Visual Metaphor

> [!quote]  
> An operating system is like a toy shop manager

- Direct operational resources
	- OS: control use of CPU, memory, peripheral devices…
	- Manager: control use of employee time, parts and tools
- Enforce working policies
	- OS: e.g. fair resources access, limit to resource usage…
	- Manager: fairness, safety, clean up
- Mitigate difficulty of complex tasks
	- OS: abstract hardware details
	- Manager: simplifies operations / Optimize performance

## What is an Operation System?
* Hide hardware complexity
* Resource management
* Provide isolation & protection

## Operation System Definition
![[Pasted image 20230826150957.png]]
## OS Elements
* Abstractions
	* process, thread, file, socket, memory page
* Mechanisms
	* create, schedule, open, write, allocate
* Policies
	* least-recently used (LRU), earliest deadline first(EDF)
## OS Design Principles
* Separation of mechanism & policy
	* Implement flexible mechanisms to support many policies
* Optimize for common case
	* Where will the OS be used?
	* What will the user want to execute on that machine?
	* ...
## User / Kernel Protection Boundary
> [!quote]  
> In order for OS to manage hardware, it shall have a privileged access called kernel -level, compared to user-level
* User-level
	* applications
* Kernel-level
	* OS kernel
	* privileged direct hardware access
* User-Kernel switch is supported by Hardware;
	* Trap instructions
	* system call
		* open, send, mmap
	* Signals
## System Call Flowchart
* To make a system call an application mush
	* write arguments
	* save relevant data at well-defined location
	* make system call
	* ![[Pasted image 20230826153832.png]]
## Crossing the OS Boundary
* *