## What is a Data Insensitive Application

- An application is data intensive if the amount of data that it generates/uses increases quickly or if the complexity of data that it generates/uses increases quickly or if the speed of change in data increases quickly.

## Reliability

- **Hardware faults**
	- Until recently redundancy of hardware components was sufficient for most applications. As data volumes increase, more applications use a larger number of machines, proportionally increasing the rate of hardware faults. **There is a move towards systems that tolerate the loss of entire machines**. A system that tolerates machine failure can be patched one node at a time, without downtime of the entire system (_rolling upgrade_).
- **Software errors**
	- It is unlikely that a large number of hardware components will fail at the same time. Software errors are a systematic error within the system, they tend to cause many more system failures than uncorrelated hardware faults.
- **Human errors**
	- Humans are known to be unreliable. Configuration errors by operators are a leading cause of outages. You can make systems more reliable:
		- Minimising the opportunities for error, peg: with admin interfaces that make easy to do the "right thing" and discourage the "wrong thing".
		- Provide fully featured non-production _sandbox_ environments where people can explore and experiment safely.
		- Automated testing.
		- Quick and easy recovery from human error, fast to rollback configuration changes, roll out new code gradually and tools to recompute data.
		- Set up detailed and clear monitoring, such as performance metrics and error rates (_telemetry_).
		- Implement good management practices and training.

## Scalability
- This is how do we cope with increased load. We need to succinctly describe the current load on the system; only then we can discuss growth questions.
- **Describing Load**
	- load parameter
		- The best choice of parameters depends on the architecture of your system:
			- requests per second to a web server,
			- the ratio of reads to writes in a database,
			- the number of simultaneously active users in a chat room
			- ...
- **Describing Performance**
	- What happens when the load increases:
		- How is the performance affected?
		- How much do you need to increase your resources?
	- Batch Processing System
		- throughput
			- The number of records we can process per second
			- The total time it takes to run a job on a dataset with certain size
	- Online System
		- response time
			- The time between a client sending a request and receiving a response
			- _Median_ (_50th percentile_ or _p50_).
			- Percentiles _95th_, _99th_ and _99.9th_ (_p95_, _p99_ and _p999_) are good to figure out how bad your outliners are.
				- Amazon describes response time requirements for internal services in terms of the 99.9th percentile because the customers with the slowest requests are often those who have the most data. The most valuable customers.
				- On the other hand, optimizing for the 99.99th percentile would be too expensive.
- **Approaches for Coping with Load**
	- 

## Maintainability
