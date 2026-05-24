### What's the difference between a process and a thread?
- A process is an independent program running in its own memory space
while a thread is the smallest unit of execution within a process.
- Threads enable a program to perform multiple tasks concurrently while sharing the same memory
and resources.
- Example: In a web server like Nginx, you might use multiple threads to handle requests
so they can share cached data.


### What are the different states of the process?
Processes can be in one of three states: running, ready, or waiting.


### What's the difference between heap and stack memory?
The stack and heap are two regions of memory in a process, but they're used very differently.
<br>
**Stack:**
- Stores local variables and function calls.
- LIFO
- Memory is freed automatically once function ends.
- If too many function calls exceed the stack's capacity, it results in a stack overflow error.
- Memory is allocated in contiguous blocks within the call stack.

**Heap:**
- Used for dynamic allocation.
- requires manual deallocation (In C/C++) or a garbage collector (in Java or Python).
- Stores larger and complex data structures like objects.
- Heap memory persists as long as the entire application is running.


### What is a deadlock, and what conditions are required for one to occur?
A deadlock happens when two or more threads are each waiting for a resource held by the other,
so none can proceed. There are four necessary conditions:
- Mutual exclusion: resources can't be shared.
- Hold and wait: a thread holds one resource while waiting for another.
- No preemption: the OS can't forcibly take a resource away.
- Circular wait: Thread A waits for B, B waits for C, C waits for A.
<br>

To prevent deadlocks, you can break any of these - for example, enforce a strict order for acquiring
locks so circular wait can't happen.
<br>
Example: Thread A locks file 1 and asks for file 2; Thread B locks file 2 and asks for file 1.


### How does a CPU scheduler work? Name a few scheduling algorithms.
The scheduler decides which runnable thread/process gets CPU time. Common algorithms:
- FCFS (First Come First Served): simple but causes the convoy effect.
- Round Robin: each process gets a fixed time slice; good for responsiveness.
- Priority scheduling: higher priority runs first, but can starve low priority ones.
- Multilevel feedback queue: used in modern OSes like Linux;
processes move between queues based on behaviour (e.g., I/O-bound gets higher priority).


### What is virtual memory?
Uses a part of disk to trick programs into thinking theres larger RAM space.


### What's the difference between paging and segmentation?
Both are memory management techniques.
- Paging divides physical and virtual memory into fixed-size blocks called 'pages'.
The OS uses a page table to map virtual addresses into the RAM.
- Segmentation divides memory into variable-sized logical segments (code, heap, stack).
- Paging is the standard and avoids fragmentation.


### What is a race condition? How do you prevent it?
A race condition happens when the outcome of a program depends on the
unpredictable timing of two or more threads accessing shared data.
- To prevent race conditions, you need synchronisation e.g. using a mutex (mutual exclusion)
to ensure only one thread accesses the shared resource at a time.
- Can also use atomic operations, semaphores, or lock-free data structures.


### What's a semaphore?
A semaphore is a synchronization tool used in operating systems to manage access
to shared resources in a multi-process or multi-threaded environment.
<br>
It is an integer variable that controls process execution using atomic operations
like wait() (decrements, acquires a resource) and signal() (increments, releases a resource)


### What's an atomic operation?
An atomic operation executes without interruption of any other process in between their execution phase.
When an atomic operation is in its executing process, no other process can read, modify,
or interrupt that operation's data.
- Small Atomic Operation: can be implemented with no interruption of any other process.
Can't break down because they're at their smallest level. E.g. Loading/storing value in registers.
- Large Atomic Operation: group of small atomic operations, e.g. calling a method.