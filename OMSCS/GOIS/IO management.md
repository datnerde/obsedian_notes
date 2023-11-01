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
- 