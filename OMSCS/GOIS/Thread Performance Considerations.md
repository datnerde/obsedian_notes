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
## Asynchronous I/O Operations
- process/thread makes system call
- OS obtains all relevant info from stack, and either learns where to return results, or tells caller where to get results later
- process/thread can continue
- Requires support from kernel and / or device
- Fits nicely with event-driven model
## What if Async Calls are not available
- AMPED 
![[Pasted image 20230930155429.png]]
- Helpers
	- designated for blocking I/O operations only
	- pipe/socket based comm with event dispatcher
		- select() and poll() are still OK
	- helper blocks, but main event loop will not
- benefits
	-  resolve portability limitations of basic event-driven model
	- smaller footprint than regular worker thread
- cons
	- applicability to certain classes of applications
	- event routing on multi CPU systems
# Flash Web Server
![[Pasted image 20230930170643.png]]
- an event-driven web server (AMPED)
- with asymmetric helper processes
- helpers used for disk reads
- pipes used for comm with dispatcher
- helper reads file in memory (via mmap)
- dispatcher checks (via mincore) if pages are in memory to decide "local handler" or helper
- Additional Optimization
	- application-level caching (data and computing)
	- alignment for DMA
	- use of DMA with scatter-gather => vector I/O operations
# Apache Web Server
![[Pasted image 20230930171900.png]]

# Experimental Methodology
- What systems are you comparing? (Define Comparison Points)
	- MP (each process single thread)
	- MT (boss-worker)
	- single process event-driven (SPED)
	- Zeus (SPED w/2 processes)
	- Apache (v.1.3.1, MP)
	- AMPED (Flash)
- What workloads will be used? (Define inputs)
	- Realistic request workload
		- distribution of web page accesses over time
	- Controlled, reproducible workload
		- trace-based (from real web servers)
	- CS Web Server Trace (Rice Univ)
	- Owlent trace (Rice Univ)
	- Synthetic workload
- How will you measure performance? (Define metrics)
	- bandwidth == bytes / time
		- total bytes transferred from files / total time
	- Connection rate == request / time
		- total client conn / total time
	- evaluate both as a function of file size
	- larger file size => ammortize per connection cost => high bandwidth
	- larger file size => more work per connection => lower connection rate
# Experimental Results
- synthetic load
	- N requests for same file => best case
- measure bandwidth
	- bw = N * bytes (F) / time
	- File size 0-200 KB
	- vary work per request
- 