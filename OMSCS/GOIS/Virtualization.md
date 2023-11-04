# What is Virtualization
- virtualization allows concurrent execution of multiple OSs (and their applications) on the same physical machine
- virtual resources == each OS thinks that it "owns" hardware resources
- virtual machine (VM) == OS + applications + virtual resources (guest domain)
- virtualization layer == management of physical hardware (virtual machine monitor, hypervisor)
![[Pasted image 20231103191843.png]]
# Defining Virtualization
- A virtual machine is an efficient, isolated duplicate of the real machine
- supported by a virtual machine monitor (VMM)
	- fidelity: provides environment essentially identical with the original machine
	- performance: programs show at worst only minor decrease in speed
	- safety & isolation: VMM is in complete control of system resources
# Benefits of Virtualization
- consolidation
	- decrease cost, improve manageability
- migration
	- availability, reliability
- security
- debugging
- support for legacy OSs
# Virtualization Models Bare Metal
- Bare-metal or hypervisor-based (type 1)
	- VMM(hypervisor) manages all hardware resources and supports execution of VMs
	- privileged, service VM to deal with devices (and other configuration and management task)
	- Xen (open source or Citrix XenServer)
		- dom0 and domUs
		- drivers in dom0
	- ESX (VMware)
		- manage open APIs
		- drivers in VMM
		- used to have Linux control core, now remote APIs
- Hosted (type 2)
	- host OS owns all hardware
	- special VMM module provides hardware interfaces to VMs and deals with VM context switching
	- KVM (kernel-based VM)
		- based on Linux
		- KVM kernel module + QEMU for hardware virtualization 
		- leverages Linux open-source community
# Virtualization Requirements
![[Pasted image 20231104131742.png]]
# Hardware Protection Levels
- commodity hardware has more than 2 protection levels
- e.g. x86 has 4 protection levels(rings)
	- and 2 protection modes
	- non-root: VMs:
		- ring 3: apps
		- ring 0: OS
	- root:
		- ring 0: hypervisor
- Switch between two modes
![[Pasted image 20231104132242.png]]
# Processor Virtualization
