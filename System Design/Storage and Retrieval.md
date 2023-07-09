# Type of Database
- OLTP - Online Transaction processing database are optimized for latency.
	- E.g. MySQL, Oracle.
- OLAP - Online Analytical processing databases are optimized data crunching! 
	- Data Warehousing 
		- Star schema: Snowflake schema is just start schema with further normalization in dimension tables
		- Column oriented: 
			- Store data in each column so that we avoid scanning all rows data
			- Perform Column compression to save space
		- Data Cubes/Materialized view 
			- optimized for reads/queries. 
			- Lack of flexibility.
		- E.g. Hbase, Hive, Spark,
- ![[Pasted image 20230709171156.png]]
# Database Index
- An Index is an additional structure that is derived from the primary data. A well chosen index optimizes for reads but slows down the write.
- Simple database index is a Hash based Index. Some issues for an index:
	-  File format (encoding)
	- Deleting records
	- Crash recovery
	- Partially written records
	- Concurrency control
	- Range queries
- More about index![[Pasted image 20230709171832.png]]
# Storage Engines
* Log-structured - LSM-Trees: SSTables
	* HBase, Cassan
	* ![[Pasted image 20230709171706.png]]
	* ![[Pasted image 20230709171731.png]]
* Page-Oriented - B-trees: RDBMS
	* ![[Pasted image 20230709171740.png]]
	* ![[Pasted image 20230709171802.png]]