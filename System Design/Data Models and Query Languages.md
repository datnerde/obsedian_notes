[[DDIA Notes]]
## Data Model
- ![[Pasted image 20230704165926.png]]
- Relational model
	- The roots of relational databases lie in business data processing, transaction processing and batch processing.
	- The goal was to hide the implementation details behind a cleaner interface.
- Document based model
	-  target use cases where data comes in self-constrained documents and relationships between one document and another are rare
- Graph model
	-  go in the opposite direction, targeting use cases where anything is potentially related to everything.
## Data Model Comparison
- The main arguments in favor of the document data model are
	-  schema flexibility, 
	- better performance due to locality, 
	- and sometimes closer data structures to the ones used by the applications. 
- The relation model counters by providing 
	- better support for joins,
	-  and many-to-one and many-to-many relationships.
## Query Language
-  imperative: MapReduce
	- tell exactly how to perform certain operation in a certain order.
-  declarative
	-  just specify the pattern
