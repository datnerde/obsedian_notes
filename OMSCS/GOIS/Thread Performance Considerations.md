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
	- 
