# Why PRC?
![[Pasted image 20231112212112.png]]
# Benefits of RPC
![[Pasted image 20231112212303.png]]
# RPC Requirements
![[Pasted image 20231112232215.png]]
# Structure of RPC
![[Pasted image 20231112232833.png]]
# Steps in RPC
![[Pasted image 20231113123029.png]]
#  Interface Definition Language
- What can the server do?
- What arguments are required for the various operations? We need an agreement
- Why 
	- client-side bind decision
	- runtime to automate stub generation
# Specifying an IDL
- An IDL used to describe the interface the server exports:
	- procedure name, arg & results types
	- version  number
- RPC can use IDL that is (only for the interface)
	- language-agnostic
	- language-specific
# Marshalling / Un-marshalling
![[Pasted image 20231113123959.png]]
![[Pasted image 20231113124215.png]]
# Binding and Registry
- Client determines
	- which server should it connect to
	- how will it connect to that server
- Registry == database of available services
	- search for service name to find service (which) and contact details (how)
	- distributed
		- any RPC service can register
	- machine-specific
		- for services running on same machine
		- client must know machine address
			- registry provides port number needed for connection
	- needs naming protocol
		- exact match for "add"
		- or consider "summation","sum","addition"
- Visual metaphor
![[Pasted image 20231113124747.png]]
# Pointers in RPCs
- no pointers 
- serialize pointers; copy referenced ("pointed to") data structure to send buffer
# Handling Partial Failures
- When a client hangs, what is the problem?
	- server down? service down? network down? message lost?
	- timeout and retry => no guarantees!
- special RPC error notification (signal, exception...)
	- catch all possible ways in which the RPC can (partially) fail
# RPC Design Choice Summary
- Binding => how to find the server
- IDL => how to talk to the server; how to package data
- Pointers as arguments => disallow or serialize pointer data
- Partial failures => special error notifications
# What is SunRPC?
![[Pasted image 20231113131035.png]]
# SunRPC Overview
![[Pasted image 20231113131621.png]]
- Oracle purchased Sun and maintained it
	- TI-RPC == Transport- Independent Sun RPC
# SunRPC XDR Example
![[Pasted image 20231113132305.png]]
# Compiling XDR
![[Pasted image 20231113132535.png]]
![[Pasted image 20231113132548.png]]
# Summarizing XDR Compilation
![[Pasted image 20231113132921.png]]
![[Pasted image 20231113133029.png]]
# SunRPC Registry
![[Pasted image 20231113133431.png]]
# SunRPC Binding
![[Pasted image 20231113133610.png]]
# XDR Data Types
- Default Types
	- char, byte, int, float
- Additional XDR types
	- const (# define)
	- hyper (640bit integer)
	- quadruple (128-bit float)
	- opaque (~ C byte)
		- uninterpreted binary data
- Fixed-length array
	- e.g., int data \[80]
- Variable-length array
	- e.g., int data <80>
		- translates into a data structure with "len" and "val" fields
- except for strings
	- string line <80> => C pointer to char
	- stored in memory as a normal null-terminated string
	- encoded (for transmission) as a pair of length and data
# XDR Routines
![[Pasted image 20231113134904.png]]
# Encoding (What goes on the wire)
- RPC header
	- service procedure ID, version number, request ID...
- Actual data
	- arguments or results
	- encoded into a bytestream depending on data type
- Transport header
	- e.g., TCP, UDP
# XDR Encoding
- XDR == IDL + the encoding
	- i.e., the binary representation of data "on-the-wire"
- XDR Encoding Rules
	- all data types are encoded in multiples of 4 bytes
	- big endian is the transmission standard
	- two's complement is used for integers
	- IEEE format is used for floating point
- Example
![[Pasted image 20231113135518.png]]
# Java RMI
![[Pasted image 20231113135916.png]]