### What's the difference between an Array and a Linked List?
- Array: Contiguous memory block. Fixed size.
- Linked List: Nodes scattered in memory, each pointing to the next. Dynamic size.

### What is a Stack? Give an example use case.
A stack is a LIFO (Last In, First Out) data structure. Main operations: push, pop, peek.
Use cases: Function call stack (recursion), undo/redo in editors, expression evaluation
(e.g., checking balanced parentheses).

### What is a Queue? Give an example use case.
A queue is a FIFO (First In, First Out) data structure. Operations: enqueue, dequeue.
Use cases: Task scheduling (printer queue, CPU process queue), breadth‑first search, message queues.

### Explain hashing and hash tables. How do you handle collisions?
A hash table maps keys to values using a hash function that computes an index into an array.
Collisions (two keys hash to same index) are handled by:
- Chaining: each array slot points to a linked list of entries.
- Open addressing: find another free slot (linear probing, quadratic probing, double hashing).

### What's the difference between a Binary Tree and a Binary Search Tree?
- Binary Tree: each node has at most two children, with no ordering constraint.
- Binary Search Tree (BST): left child's key < parent's key < right child's key (for all nodes).
This ordering enables O(log n) search, insert, delete when balanced.

### What is recursion? What are its advantages and disadvantages?
Recursion is when a function calls itself to solve a smaller instance of the same problem.
Advantages: Clean, readable code for problems like tree traversals, divide‑and‑conquer.
Disadvantages: Risk of stack overflow (deep recursion), higher memory usage, sometimes slower than iteration.

### What is a heap (data structure)? What is it used for?
A heap is a complete binary tree where each node satisfies the heap property:
- Max‑heap: parent ≥ children.
- Min‑heap: parent ≤ children.

Used for priority queues, heap sort, and finding kth smallest/largest elements.
Operations: insert O(log n), extract min/max O(log n), peek O(1).

### Explain the difference between a shallow copy and a deep copy.
- Shallow copy: copies only the references/pointers, not the actual objects.
Both original and copy share the same underlying data.
- Deep copy: recursively copies all nested objects. Original and copy are completely independent.

### What is Big O notation? Why is it important?
Big O describes the upper bound of an algorithm's time or space complexity as input size grows,
ignoring constants and lower‑order terms.
It's important for comparing algorithm efficiency and scalability independently of hardware or language.

### What is the difference between an ArrayList and a LinkedList in Java?
- ArrayList: backed by a dynamic array. Fast random access O(1), slow insert/delete in middle O(n).
- LinkedList: doubly linked list. Slow random access O(n),
fast insert/delete at ends O(1) and O(n) to find position first.

### What is a priority queue? How is it usually implemented?
A priority queue is a data structure where each element has a priority.
The element with the highest priority is removed first.
It's typically implemented using a heap (usually binary heap) for O(log n) insert and remove.

### Explain the difference between a depth‑first search (DFS) and breadth‑first search (BFS).
- DFS: explores as far as possible along a branch before backtracking. Uses a stack (or recursion).
- BFS: explores all neighbours at current depth before moving deeper. Uses a queue.

Use DFS for topological sorting, cycle detection; BFS for shortest path in unweighted graphs.

### What is a graph? How do you represent it in code?
A graph consists of vertices (nodes) and edges (connections). Common representations:
- Adjacency matrix: 2D array of size V×V; O(1) edge lookup but O(V²) space.
- Adjacency list: array of lists for each vertex; O(V+E) space, better for sparse graphs.

### What is the difference between a stable and an unstable sorting algorithm?
- Stable sort: preserves the relative order of equal elements.
Example: Merge sort, Insertion sort, Bubble sort.
- Unstable sort: may change the relative order of equal elements.
Example: Quick sort (typically), Heap sort, Selection sort.

### What is a trie (prefix tree)? When would you use it?
A trie is a tree‑like data structure used to store a dynamic set of strings, usually for fast prefix searches.
Each node represents a character; paths from root represent words.
Use cases: autocomplete (search bar), spell checker, IP routing (longest prefix match),
dictionary lookup with O(L) time where L is word length.
