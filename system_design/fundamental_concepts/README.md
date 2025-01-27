## System Design Fundamental Concepts

### Characteristics

#### Scalability

- Ability to handle growing demands.
- Horizontal Scaling: Adding more servers
- Vertical Scaling: Adding more resources

#### Reliability

- Ensures that a system functions correctly, handles errors, and secures against unauthorised access.
- System functions correctly even when components fail.

#### Availability

- The percentage of time a system remains operational.
- Often expressed in 9s, e.g. 99.9% availability means the system is down for no more than 8.76 hours per year, while 99.99% would only be down for 52.6 mins per year.

- **Rate Limiting**:
    - Rate limiting controls service use by setting a cap on the number of operations within a specified time.
    - This strategy prevents service overuse, maintaining availability by managing load and reducing unnecessary costs.
    - Helps prevent DDoS (Distributed Denial of Service) attacks.
    - **_Techniques_**:
        - **Token bucket**: Allocates a certain number of tokens per request, limiting service when the bucket is empty.
        - **Leaky bucket**: Discards excess requests when capacity is reached.
        - **Fixed and sliding window**: Controls request spikes by limiting the number in a set window of time.

- **Queue-Based Load Leveling**:
    - Manages service demand by introducing a queue that moderates the flow of tasks to services, preventing system overload.

- **Gateway Aggregation**:
    - Reduces multiple service requests into a single operation at the gateway level, improving efficiency and reducing the load on backend services.

#### Efficiency

- **Latency**:
    - Delay in first response.
- **Throughput**:
    - Number of operations handled in a given time.


### CAP Theorem

- The CAP Theorem states that a distributed system can only guarantee 2 out of the 3 properties:
    - **Consistency**:
        - All nodes display identical data, guaranteeing that reads always reflect the most recent write.
    - **Availability**:
        - Every request receives a response, without guarantee that it contains the most recent write.
    - **Partition Tolerance**:
        - The system continues to operate despite network partitions (communications break within a distributed system - a lost or temporarilty delayed connection between two nodes).


### Load Balancer:

- Load balancers distribute incoming requests across multiple servers to ensure one server does not get overwhelmed.
- They can be placed at various levels:
    - Between users and web servers
    - Between web servers and application servers
    - Between application servers and databases
- One load balancer could become a single point of failure, so we can add another one for standby.
- Advantages include scalability, reliability, and performance.

#### Algorithms

- **Round robin**:
    - Cycle through servers in sequential order, ensuring even distribution.
- **Least connection**:
    - Directs traffic to the server with the fewest active connections.
- **Consistent hashing**:
    - Routes requests based on criteria like IP address or URL, useful in maintaining user session consistency.


### APIs

- **REST API**:
    - Allows stateless communication and resource manipulation using standard HTTP methods (GET, POST, PUT, DELETE).
- **RPC (Remote Procedure Call)**:
    - Streamlines back-end data exchanges using binary data for lightweight communication.
- **SOAP (Simple Object Access Protocol)**: 
    - Uses xml format to ensure high security, suitable for transactions requiring strict compliance.
- **GraphQL**:
    - Allows clients to define precisely what data they need, optimizing flexibility and reducing data transfer.


### Caching

- Caching speed up data retrieval and is much faster than retrieving data from the database.
- *CDNs (Content Delievery Network)* are ideal for serving static media, they cache data geographically closer to the user to reduce latency.

#### Types of Caching

- **In-memory cache**: Fast but increases memory usage per server.
- **Distributed cache**: Shares cache across all servers, e.g., Memcached, Redis.
- **Database cache**: Caches frequent queries or results.
- **File system cache**: Uses CDNs to cache files geographically close to users.

#### Caching Policies:

- **FIFO**: Evicts the oldest data first.
- **LRU**: Removes least recently accessed data.
- **LFU**: Discards least frequently accessed data.

#### Cache Invalidation Strategies:

- Caching has challenges with maintaining data consistency and making sure the data is in sync with the source of truth.

- **Write-Through**:
    - Data is written to both cache and storage at the same time ensuring consistency but increasing write latency.
- **Write-Around**:
    - Data bypasses the cache and goes directly to the storage preventing cache flooding but potentially increasing read latency for new data.
- **Write-Back**:
    - Data is written to cache first and later to storage, offering low latency but risking data loss in case of system failures.


### Database: SQL vs NoSQL

#### SQL/Relational Databases

- SQL/Relational databases are structured and handle complex queries and relationships among multiple tables using primary and foreign keys.
- Difficult to scale horizontally.
- *ACID Compliance*:
    - **Atomicity**: Ensures that a transaction is fully completed or not at all.
    - **Consistency**: Guarantees that a transaction takes a database from one valid state to another, enforcing all defined rules.
    - **Isolation**: Keeps transactions separate so operations don't interfere with each other.
    - **Durability**: Ensures that once a transaction is committed it remains permanent even in case of failure.
- Examples: Amazon RDS, MySQL, PostgreSQL

#### NoSQL/Non-relational Databases

- NoSQL databases are designed for flexibility and have unstructured data.
- They are good for horizontal scaling and large volumes of data.
- Diverse data types: Supports documents, key-value pairs, and wide-column stores.


### Database Sharding

- Database sharding involves dividing a large database into smaller, more manageable pieces, known as shards, each hosted on separate servers.
- Improves performance, availability, and scalability.


### Database Replication

- Database replication involves copying data from one database to one or more databases. This can safeguard against data loss during failures, improve data access speed for users in different geographical locations, and help scale applications by distributing the load.