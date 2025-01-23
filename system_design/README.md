## System Design Interview Notes

### How to answer
Notes from https://www.tryexponent.com/blog/system-design-interview-guide

#### 1. Understand the problem

- Ask questions about the problem and define the scope of the design
- What are the functional and non-functional requirements?
- What should be included and excluded?
- Who are the clients and consumers?

#### 2. Clarify non-functional requirements

- Ask about availability, consistency, speed, security, reliability, maintainablity, cost.
- What is the scale of the system?
- How many users should it support?
- How many requests should the server handle?
- Are most use cases read-only?
- Do users typically read the data shortly after someone else overwrites it?

#### 3. Estimate Data

- Queries per second
- Storage Size
- Bandwidth requirements

#### 4. High-level System Design

- Design API and choose what type
    - REST (Representational State Transfer)
    - SOAP (Simple Object Access Protocol)
    - RPC (Remote Procedure Call)
    - GraphQL

- Data Modelling
    - Create simple schemas with only important fields
    - Discussing data access patterns and the read-to-write ratio
    - Identify what type of database to use (Structured or unstructured)

- Design Diagram and confirm it satisfies all functional requirements

#### 5. Deep-Dive

- Consider how non-functional requirements impact design choices.
    - Transactions: If the system requires transactions, consider a database that offers the ACID (Atomicity, Consistency, Isolation, and Durability) property.
    - Data freshness: If an online system requires fresh data, think about how to speed up the data ingestion, processing, and query process.
    - Data size: If the data size is small enough to fit into memory (up to hundreds of GBs), you can place it in memory. However, RAM is prone to data loss, so if you can't afford to lose data, you must find a way to make it persistent.
    - Partitioning: If the volume of data you need to store is large, you may want to partition the database to balance storage and query traffic.
    - Offline processing: If some processing can be done offline or delayed, you may want to rely on message queues and consumers.
    - Access patterns: Revisit the data access pattern, QPS number, and read/write ratio, and consider how they impact your choices for databases, database schemas, and indexing options.

#### 6. Improve the Design (Bottlenecks and scale)

- Consider single points of failure, data replicas, CDNs (Content Delivery Networks), high traffic, scalability
- Consider MQs (Message Queues) or Pub/Sub.
    - MQs are good for processing jobs in a specific order.
    - Pub/Sub is good at sending information to a large number of subscribers concurrently.
- Discuss bottlenecks and propose alternatives, trade-offs, etc.