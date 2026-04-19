---
title: System Design — Map of Content
tags: [moc, system-design, distributed-systems]
created: 2026-04-14
status: growing
---

# 🏗️ System Design — Map of Content

> Navigation hub for system design notes.  
> Primary source: *Designing Data-Intensive Applications* (DDIA) by Martin Kleppmann.

---

## 📖 Source
- *Designing Data-Intensive Applications* (DDIA) — Martin Kleppmann
- Compiled into atomic notes below

---

## 🗂️ Topics (by DDIA chapter order)

### Foundations
- [[Reliable, Scalable and Maintainable]] 🌿
  - Reliability: hardware faults, software errors, human errors
  - Scalability: load parameters, throughput, latency percentiles
  - Maintainability: operability, simplicity, evolvability

### Storage
- [[Data Models and Query Languages]] 🌿
  - Relational vs document vs graph models
- [[Storage and Retrieval]] 🌿
  - Log-structured (LSM trees, SSTables)
  - Page-oriented (B-trees)
  - OLTP vs OLAP
- [[Encoding and Evolution]] 🌿
  - JSON, Thrift, Protobuf, Avro

### Distributed Systems
- [[Replication]] 🌿
  - Leader-follower, multi-leader, leaderless
  - Replication lag, read-your-writes, monotonic reads

---

## 🔗 Key Concepts Map

```
Reliability ──────────────────────────────────────┐
Scalability (load params → throughput/latency)     ├── Ch.1
Maintainability ───────────────────────────────────┘

Data Models (relational/doc/graph) ────────────────┐
Query Languages (SQL/MapReduce) ────────────────────┤── Ch.2-3
Storage Engines (LSM/B-tree) ──────────────────────┘

Replication (leader/leaderless) ───────────────────── Ch.5
```

---

## 🌱 To Be Added (DDIA Chapters 6–12)
- `Partitioning` (sharding)
- `Transactions` (ACID, isolation levels)
- `Distributed System Troubles` (network faults, clocks)
- `Consistency & Consensus` (linearizability, Raft)
- `Batch Processing` (MapReduce)
- `Stream Processing` (Kafka, event sourcing)

---

## 💼 Interview Prep Checklist
- [ ] Explain CAP theorem with real examples
- [ ] Design a URL shortener
- [ ] Design a rate limiter
- [ ] Design a distributed cache

---

*[[INDEX]] | [[CLAUDE]]*
