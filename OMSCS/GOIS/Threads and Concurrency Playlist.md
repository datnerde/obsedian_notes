![[Pasted image 20230827125300.png]]
# Visual Metaphor
>[!quote]
> A thread is like a worker in a toy shop
* is an active entity
	* executing unit of a process
* works simultaneous with others
	* many threads executing
* requires coordination
	* sharing of I/O devices, CPUs, memory
# Process v.s. Thread
![[Pasted image 20230827130011.png]]
# Benefits of Multithreading
- Parallelization => Speed UP
- Specialization => Hot Cache!
- Efficiency => lower memory management requirement& cheaper IPC

# Benefits of Multithreading:  # threads > # CPUs
![[Pasted image 20230827171717.png]]
- if (t_idle)>2*(t_ctx_switch) then context switch to hide idling time
- t_ctx_switch threads < t_ctx_switch process