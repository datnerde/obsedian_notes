![[Pasted image 20231101081920.png]]
# I/O Device Features
![[Pasted image 20231101133943.png]]
# CPU Device Interconnect
![[Pasted image 20231101140123.png]]
# Device Drivers
- per each device type
- responsible for device access, management and control
- provided by device manufacturers per OS/version
- each OS standardizes interfaces
	- device independence
	- device diversity
# Types of Devices
- Block: disk
	- read/ write blocks of data
	- direct access to arbitrary block
- Character: keyboard
	- get/put character
- Network devices
- OS presentation of a device == special device file
	- ![[Pasted image 20231101141802.png]]
# CPU Device Interactions
- access device registers == memory load / store
- memory-mapped I/O
	- part of host physical memory dedicated for device interactions
	- base address registers (BAR)
- I/O port
	- dedicated in/out instructions for device access
	-  target device (i/o port) and value in register
- Path from Device to CPU
	- Interrupt (device generate)
		- - interrupt handling steps
		- + can be generated as soon as possible
	- Polling (CPU to call device)
		- + when convenient for OS
		- - delay or CPU overhead
# Device Access POI (Programmed I/O)
- no additional hardware support
- CPU 'programs' the device
	- via command registers
	- data movement
- Example: NIC, data == network packet
	- write command to request packet transmission
	- copy packet to data registers
	- repeat until packet sent
	- Example:
		- ![[Pasted image 20231101181003.png]]
# Device Access DMA (Direct Memory Access)
- relies on DMA controller
- CPU programs the device
	- via command registers
	- via DMA controls
- Example:
	- write command to request packet transmission
	- configure DMA controller with in-memory address and size of packet buffer
- ![[Pasted image 20231101181524.png]]
- data buffer must be in physical memory until transfer completes ==> pinned region

# Typical Device Access
![[Pasted image 20231101194251.png]]
# OS Bypass
