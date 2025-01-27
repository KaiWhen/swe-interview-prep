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

#### Algorithms

- **Round robin**:
    - Cycle through servers in sequential order, ensuring even distribution.
- **Least connection**:
    - Directs traffic to the server with the fewest active connections.
- **Consistent hashing**:
    - Routes requests based on criteria like IP address or URL, useful in maintaining user session consistency.