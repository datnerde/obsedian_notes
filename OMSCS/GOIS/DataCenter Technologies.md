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
- All equal:  all nodes execute any possible step in request processing, for any request
- Specialized nodes: nodes execute some specific steps in request processing, for some request types
- functionaly homogeneous / functionaly heterogeneous
# Homogeneous Architectures
- functionaly homogeneous
	- can do any processing step
	- + keep front-end simple
		- doesn't mean that each nodes has all data; just each node can get to all data
	- - how to benefit from caching?
![[Pasted image 20231204155639.png]]
# Heterogeneous Architectures
- functionaly heterogeneous
	- different nodes, different tasks / requests
	- data doesn't have to be uniformly accessible everywhere
	- + benefit of locality and caching
	- - more complex FE
	- - more complex management
![[Pasted image 20231204160011.png]]
![[Pasted image 20231204162335.png]]
# Cloud Computing Poster Child: Animoto
- Amazon
	- provisioned hardware resources for holiday sale season
	- resources idle the rest of the year
	- opened access to its resources via web-based APIs
	- third party workloads on Amazon hardware for a fee
	- => Amazon Web Services(AWS) and Amazon's Elastic Compute Cloud (EC2)
- Animoto rented comput instances in EC2
	- become available to Facebook Users
	- EC2 scale crazy
# Cloud Computing Requirements
- Traditional Approach
	- buy and configure resources
		- determine capacity based on expected demand (peak)
	- when demand exceeds capacity
		- dropped requests
		-  lost opportunity
- Ideal Cloud
	- capacity scales elastically with demand
	- scaling in instantaneous, both up and down
		- cost is proportional to demand, to revenue opportunity
	- all of this happens automatically no need for hacking wizardry
	- can access anytime anywhere
	- done't own resources
- Summarized
	- On-demand. elastic resources and services
	- fine-grained pricing based on usage
	- professionally managed and hosted
	- API-based access
# Cloud Computing Overview
![[Pasted image 20231204170346.png]]
# Why Does Cloud Computing Work
![[Pasted image 20231204170508.png]]
# Cloud Computing Vision
![[Pasted image 20231204170823.png]]
# Cloud Deployment Models
- Public
	- third party customers / tenants
- Private
	- leverage technology internally
- Hybrid (Public + Private)
	- failover, dealing with spikes, testing
- Community
	- used by certain type of users
# Cloud Service Models
![[Pasted image 20231204172921.png]]
# Requirements for the Cloud
- fungible resources
- elastic, dynamic resource allocation methods
- scale: management at scale, scalable resources allocations
- dealign with failures
- multi-tenancy: performance & isolation
- security
# Cloud Enabling Technologies
- Virtualization
- Resources provisioning (scheduling)
	- mesos, yarn
- big data processing (hadoop, mapreduce, spark)
	- storage
		- distributed FS
		- no sql, distributed in-memory caches
- Software - befined .. networking, storage, datacenters
- monitoring == real time log processing (flume, cloudwatch, log insight)
# The Cloud as a Big Data Engine
- data storage layer
- data processing layer
- caching layer
- language front-ends
- analytics libraries
# Example Big Data Stacks
