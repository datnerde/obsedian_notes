---
title: Replication
tags: [system-design, replication, distributed-systems, ddia]
created: 2026-04-14
status: growing
related: [[Reliable, Scalable and Maintainable]], [[Storage and Retrieval]], [[OMSCS/GOIS/Distributed Shared Memory]]
source: Designing Data-Intensive Applications Ch.5
---

# Replication

## Core Idea
Keep a copy of the same data on multiple machines (replicas) to achieve fault tolerance, increase read throughput, and reduce latency for geographically distributed users.

## Why Replication Is Hard
Data changes over time. The challenge is keeping replicas in sync when writes happen.

## Replication Strategies

### Single-Leader (Master-Follower)
- All writes go to the leader
- Leader sends a replication log to followers
- Reads can go to any follower (eventual consistency) or leader (strong consistency)
- **Failover**: if leader dies, a follower is elected as new leader
- Used by: MySQL, PostgreSQL, MongoDB

### Multi-Leader
- Multiple nodes accept writes (one per datacenter typically)
- Conflict resolution needed when two leaders accept writes to the same record
- Use case: multi-datacenter deployments, offline-first clients
- Problem: **write conflicts** — last-write-wins, merge, or application-level resolution

### Leaderless (Dynamo-style)
- Any replica can accept writes
- Reads/writes go to multiple replicas; use quorum: `w + r > n`
- Examples: Cassandra, Riak, DynamoDB

## Replication Lag Problems
With asynchronous replication, followers may be seconds/minutes behind:
- **Read-your-writes**: you might not see your own write if you read from a lagging follower
- **Monotonic reads**: reading from different followers can appear to go backward in time
- **Consistent prefix reads**: causally related writes must be seen in order

## Consistency Guarantees
- **Eventual consistency**: replicas converge eventually (weakest)
- **Read-your-writes**: you always see your own writes
- **Linearizability**: strongest — behaves as if there's a single copy

## Related
- [[Reliable, Scalable and Maintainable]] — fault tolerance context
- [[Storage and Retrieval]] — what's being replicated
- [[Data Models and Query Languages]] — replication is data-model agnostic
