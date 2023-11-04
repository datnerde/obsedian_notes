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
- Bare-metal or hypervisor-based
	- VMM(hypervisor) manages all hardware resources and supports execution of VMs
	- privileged, service VM to deal with devices (and other configuration and management task)
	- Xen (open source or Citrix XenServer)
		- do
- Hosted