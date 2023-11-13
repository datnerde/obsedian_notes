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
# Marshalling
