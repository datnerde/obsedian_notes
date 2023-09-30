# Preview
- Performance comparisons
	- multi-process vs. multi-threaded vs. event-driven
- Event-driven architectures
	- "Flash" vs Apache
# Which Threading Model is Better
![[Pasted image 20230929222000.png]]
# Are Threads Useful
- parallelization => speed up
- specialization => hot cache
- efficiency => lower memory requirements and cheaper synchronization
- high latency of I/O operations
- What is useful
	- matrix multiply application
		- execution time
	- for web service application (avg / max / min/ 95%)
		- number of client requests/ time
		- response
	- hardware
		- higher utilization (e.g. CPU)
- Depends on metrics and workloads
# Thread Performance Considerations Visual Metaphor
![[Pasted image 20230930141022.png]]
# Performance Metrics
- metrics : a measurement standard
- measurable / quantifiable
- of the system we are interested in
- to evaluate the system behaviour
- examples:
	![[Pasted image 20230930141820.png]]
- experiments with real software deployment, real machines, real workloads
- 'toy' experiments representative of realistic settings
- simulation
# Multi Process vs. Multi Threaded
![[Pasted image 20230930143052.png]]
- Multi Process Web Server (MP)
	- Simple programming (+)
	- high memory usage (-)
	- costly context switch (-)
	- hard / costly to maintain shared state (-)
- Multi Threaded Web server (MT)
	- shared address space (+)
	- shared state (+)
	- cheap context switch (+)
	- not simple implementation  (-)
	- requires synchronization  (-)
	- underlying support for threads  (-)
# Event-Driven Model
![[Pasted image 20230930145358.png]]
- single address space
- single process
- single thread of control
- Dispatcher: state machine external events
- call handler: jump to code
- Hanlder
	- run to completion
	- if they need to block
		- initiate blocking operation and pass control to dispatch loop
# Concurrency in the Event Driven Model
- MP and MT:
	- 1 request per execution context
- event-driven
	- many requests interleaved in an execution context
![[Pasted image 20230930150654.png]]

# Event-Driven Model: Why
- one 1 CPU "threads high latency"
- if (t_idle > 2 * t_ctx_swithc*)
	- ctx_switch to hide latency
- if (t_idle == empty)
	- context switching just wastes cycles that could have been used for request processing
- process request until wait necessary then switch to another request
- multiple CPUs => multiple event-driven processes
# Event-Driven Model: How
- event == input on file descriptor (FD)
- which file descriptor?
	- select() : need to search a range of FD
	- poll(): need to search a range of FD
	- epoll(): reduce some search 
- benefits
	- single address space / single flow of control
	- smaller memory requirement / no context switching
	- no synchronization
- cons
	- a blocking request / handler will block the entire process
# Helper Threads and Processes
- Asynchronous I/O Operations
- 