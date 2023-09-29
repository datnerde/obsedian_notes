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
