# Introduction
---
- Web servers cache frequently request content in main memory
    - avoids disk latency inssues
- Approaches
    - single-process event-driven (SPED) architecture can provide excellent performance for cached workloads, where most requested content can be kept in main memory.
        - Ex: Zeus / Squid Proxy
    - multi-process (MP) or multi-threaded (MT) architecture
        - Ex: Apache
- Flash Server matches the performance of SPED and matches or exceeds MP/MT approaches
# Background
---
- Serving a request
    - Accept Client Connection
        - `accept` on `listen` socket
    - Read request
        - read the HTTP request header and parse the header
    - Find file
        - Check if the file exists and the client has permissions
        - File size and last modification time are obtained for inclusion in the response header
    - Send response header
        - transmit HTTP response header
    - Read file
        - read the file data (or chunks)
    - Send data
        - transmit the requested content
- All steps of serving a request can potentially block
# Server Architectures
---
## Multi-process (MP)

- Each request is assigned to one process
    - The OS takes care of switching processes (20-200 at a time)
    - No synchronization is necessary
    - But hard to optimize

## Multi-threaded (MT)

- Multiple threads in a shared address space
- Each thread manages a request (like processes are used in MP)
- Big difference is that the threads share global variables
- But, must use some form of synchronization
- The OS must support kernel threads.
    - FreeBSD does not as it only has user-level threads w/o kernel support

## Single-process event-driven (SPED)

- Single process processes HTTP requests
- Use non-blocking system calls to perform asynchronous I/O operations
    - Ex `select` on UNIX or `poll` on System V to check for I/O operations that have completed
- A SPED Server can be thought of as a state machine that performs one step of an HTTP request at a time
    - `select` is performed to check for completed I/O events
        - When one is ready, the corresponding step is carried out and the next step is initiated
- The single thread controls CPU, Disk, and Network operations
    - This avoids the overhead of context switching and thread synchronization (in the MP and MT architectures)
- The big challenge is lack of support for asynchronous disk operations
    - non-blocking `read` and `write` operations work on network sockets and pipes, but block when used on disk files
- Some UNIX systems have APIs that implment asynchronous disk I/O but they are not integrated with `select`. Also `open` and `stat` on file descriptors may still block

## Asymmetric Multi-Process Event-Drive (AMPED)

- Combines event-driven SPED architecture with multiple _helper_ processes (or threads) to handle blocking disk I/O operations
- The main process handles all HTTP request processing.
- Disk I/O is handled via IPC (pipe) to helper threads that handle the disk stuff
    - The helper returns notification via IPC
    - The main process learns of this via `select`
- In a UNIX system, AMPED uses the standard non-blocking `read`, `write`, and `accept` system calls on sockets and pipes, and the `select` system call to test for I/O completion. The `mmap` operation is used to access data from the filesystem and the `mincore` operation is used to check if a file is in main memory.

