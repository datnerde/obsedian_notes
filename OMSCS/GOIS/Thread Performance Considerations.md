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
	- 