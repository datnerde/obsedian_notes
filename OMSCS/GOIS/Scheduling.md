## Visual Metaphor

![[Pasted image 20231007164257.png]]

## Scheduling Overview

### CPU Scheduling

- CPU scheduler
	- decides how and when processes( and their threads) access shared CPU
	- schedules tasks running user-level processes / threads as well as kernel-level threads
- CPU scheduler in practice
- ![[Pasted image 20231007165653.png]]
	- chooses one of ready tasks to run on CPU
	- scheduler runs when
		- CPU becomes idle
		- new task becomes ready
		- timeslice expired timeout
	- thread is dispatched on CPU after scheduled
		- context switch
		- enter user mode
		- set PC and go
- scheduling == choose task from read queue
	- which task should be selected?
		- scheduling policy / algo
	- how is this done?
		- depends on runqueue data structure

## Run to Completion Scheduling

- Initial Assumptions
	- group of tasks / jobs
	- known execution times
	- no preemption
	- single CPU
- Metrics
	- throughput
	- avg. job completion time
	- avg.job wait time
	- CPU utilization
- First-Come First-Serve (FCFS)
	- schedules tasks in order of arrival
	- can use a queue structure for tasks
- Shortest Job First (SJF)
	- schedules tasks in order of their execution time
	- runqueue == ordered queue
		- tree structure

## Preemptive Scheduling: SFJ + Preempt

- Case:
	- ![[Pasted image 20231008135054.png]]
	- T2 should be preempted
	- T2 arrives first
- Heuristic based on history on job running time
	- how long did a task run last time
	- how long did a task run last n time

## Preemptive Scheduling: Priority

- Case:
	- ![[Pasted image 20231008135547.png]]
	- Task have different priority level
	- run highest priority task next
	- Priority: T3>T2>T1
- Two types of runqueue
	- runqueue per priority level
	- ![[Pasted image 20231008135733.png]]
	- tree ordered based on priority
- Cons
	- low priority task stuck in a runqueue => starvation
		- priority aging
			- priority = f(actual priority, time spent in runqueue)
	- prevent starvation!

## Priority Inversion

![[Pasted image 20231008140323.png]]

## Round Robin Scheduling

- pick up first task from queue (like FCFS)
- task may yield to wait on I/O (unlike FCFS)
- Round Robin with Priorities
	- include preemption
	- round robin on tasks with same priority
- Round Robin with interleaving
	- timeslicing

## Timesharing and Timeslices

- timeslicing == maximum amount of uninterrupted time given to a task => time quantum
- task may run less than timeslice time
	- has to wait on I/O, synchronization => will be placed on a queue
	- higher priority task becomes runnable
- using timeslices tasks are interleave
	- timesharing the CPU
	- CPU bound-task => preempted after timeslice  
![[Pasted image 20231008142010.png]]
- Pros
	- short tasks finish sooner
	- more responsive
	- lengthy I/O ops initiated sooner
- Cons
	- overhead
		- interrupts
		- schedules
		- context switch

## How Long Should a Timeslice Be

- Balance benefits and overheads
	- I/O bound tasks
		- ![[Pasted image 20231008145027.png]]
		- I/O bound tasks can issue I/O ops earlier
		- keeps CPU and device utilization high
		- better user-perceived performance
	- CPU bound tasks
		- ![[Pasted image 20231008144702.png]]
			- limit context switching overheads
			- keeps CPU utilization and through put

## Runqueue Data Structure

- if we want I/O and CPU bound tasks to have different timeslice values, then
	- same runqueue, check type
	- two different structures
- dealing with different timeslice values
	- ![[Pasted image 20231008153409.png]]
- because we don't know if a new task is I/O intensive and how intensive it is
	- ![[Pasted image 20231008153658.png]]
- the above design is called multi-level feedback queue (MLFQ)
	- different treatment of threads at each level
	- feedback

## Linux O(1) Scheduler

- ![[Pasted image 20231008154305.png]]
- Timeslice value
	- depends on priority
	- smallest for low priority
	- highest for high priority
- Feedback
	- sleep time: waiting / idling
	- longer sleep => interactive=> priority -5 (boosted)
	- smaller sleep => compute-intensive => priority + 5 (lowered)
- Runqueue == 2 arrays of tasks
	- Active
		- used to pick the next task to run
		- constant to add / select
		- tasks remain in queue in active array until timeslice expires
	- Expired
		- inactive list
		- when no more tasks in active array => swap active and expired
- Cons
	- affect performance of interactive tasks
	- no fairness guarantee
	- workload changes
		- replaced by CFS(completely fair scheduler)

## Linux CFS Scheduler

- a default scheduler in LINUX for non real-time tasks
- runqueue == red-black tree
	- ![[Pasted image 20231008165007.png]]
	- self-balance tree
	- ordered by 'v-runtime'
	- vruntime == time spent on CPU
- CFS scheduling
	- always pick leftmost node
	- periodically adjust vruntime
	- compare to leftmost vruntime
		- if smaller, continue running
		- if larger, preempt and place appropriately in the tree
	- vruntime progress rate depends on priority and nicesness
		- rate faster for low-priority
		- rate slower for high-priority
		- same tree for all priorities
	- Performance
		- select task => o(1)
		- add task => O(logn)

## Scheduling on Multiprocessors

- ![[Pasted image 20231008165754.png]]
	- cache-affinity important!
		- keep tasks on the same CPU as much as possible
		- hierarchical scheduler architecture
	- per-cpu runqueue and scheduler
		- load balance across CPU
			- based on queue length
			- or when CPU is idle
	- multiple memory nodes
		- memory node closer to a 'socket' of multiple processors
			- access to local memory node faster than access to remote mm node
			- keep tasks on CPU scheduler to MM node where their state is
				- NUMA-aware scheduling
- ![[Pasted image 20231008165843.png]]

## Hyperthreading

- multiple hardware-supported execution contexts
- still 1 CPU but..
- with very fast context switch
- if(t_idle)>2 x t_ctx_switch), then context switch to hide latency
	- SMT ctx_switch - O(cycles)
	- memory load - O(100 cycles)
- hyperthreading can high memory access latency

## Scheduling for Hyperthreading Platforms

- Assumptions:
	- thread issues instruction on each cycle
		- max instruction-per-cycle (IPC)= 1
	- memory access = 4 cycles
	- hardware switching instantaneous
	- SMT with 2 hardware threads
- ![[Pasted image 20231008174528.png]]
- ![[Pasted image 20231008174705.png]]
- ![[Pasted image 20231008174826.png]]

## CPU Bound or Memory Bound

- Use historical information
- "sleep time" won't work
	- the thread is not sleeping when waiting on MM
	- software takes too much time to compute
- need hardware-level information to answer the question
	- Hardware counters
		- L1, L2,… LLC misses
		- IPC
		- power and energy data
		- Software interface and tools
			- e.g., oprofile, Linux perf tool…
			- oprofile websties lists available hardware counters on different architectures
	- (g) estimate what kind of resources a thread needs
		- scheduler can make informed decisions
			- typically multiple counters
			- models with per architecture thresholds
			- based on well-understood workloads

## Scheduling with Hardware Counters

- Is cycles-per-instruction (CPI) useful?
	- memory bound => high CPI
	- CPU-bound => 1 (or low) CPI
- Experimental Methodology
	- Testbed
		- 4 cores x 4-way SMT
		- total of 16 hardware contexts
	- Workload
		- CPI of 1,6,11,16
		- 4 threads of each kind
	- Metric == IPC
		- max IPC = 4
- Experiment results
	- ![[Pasted image 20231008180405.png]]
	- Doesn't work in realist workloads
		- because real workloads with big difference in CPI values
- Post Mortem
	- Takeaways
		- resource contention in SMTs for processor pipeline
		- hardware counters can be used to characterize workload
		- schedulers should be aware of resource contention not just load balancing
	- LLC usage would have been a better choice
