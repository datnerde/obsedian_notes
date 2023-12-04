# Internet Services
- Internet Service == any type of service provided via web interface
	- presentation == static content
	- business logic == dynamic content
	- database tier == data store
- not necessarily separate processes on separate machines
- many available open source and proprietary technologies
- middleware == supporting, integrative or value-added software technologies
- in multi process configurations
	- some form of IPC used, including RPC/RMI, shared memory

# Internet Service Architectures
- For scale: multi-process, multi-node
	- scale out architecture
- Boss-worker: front-end distributes requests to nodes
- All equal:  a