# Graphics-related questions

## Describe the rendering pipeline.

1. Vertex generation: Define vertex location, normal, colour, etc.
- Each vertex retrieved from the vertex arrays (as defined by the VAO) is acted upon by a Vertex Shader. Each vertex in the stream is processed in turn into an output vertex.
2. Vertex transformation/processing: Rotate, translate, scale, distort
3. Primitive generation: Define topology
- The purpose of the primitive assembly step is to convert a vertex stream into a sequence of base primitives.
4. Primitive processing: Culling (discarding without rendering), clipping
5. Rasterisation: Identify fragments
6. Fragment processing: Lights, colour interpolation
- The data for each fragment from the rasterization stage is processed by a fragment shader. The output from a fragment shader is a list of colors for each of the color buffers being written to, a depth value, and a stencil value. Fragment shaders are not able to set the stencil data for a fragment, but they do have control over the color and depth values. 
7. Pixel operations: Test fragments and generate pixels, render image to frame buffer


# C/C++ Related

## Advantages of C++:

1. C++ is an OOPs language that means the data is considered as objects.
2. C++ is a multi-paradigm language; In simple terms, it means that we can program the logic, structure, and procedure of the program.
3. Memory management is a key feature in C++ as it enables dynamic memory allocation
4. It is a Mid-Level programming language which means it can develop games, desktop applications, drivers, and kernels

## C over C++

- C is preferred over C++ for certain applications due to its simplicity and efficiency.
- C is a simpler language compared to C++ and has a smaller runtime footprint.
- C is often used for low-level programming, embedded systems, and operating systems.
- C allows for more control over memory management and can be faster in certain scenarios.
- C++ introduces additional features like object-oriented programming and templates, which may not be necessary for all projects.

## Define 'std'

The command “using namespace std” informs the compiler to add everything under the std namespace and inculcate them in the global namespace.

## What are references in C++?

When a variable is described as a reference it becomes an alias of the already existing variable.

Syntax:
`int foo = 10;
int& ref = foo;`

## Stack vs Heap Memory Allocation

1. Stack memory is allocated in a contiguous block while heap memory is allocated in any random order.
2. In a stack, the allocation and de-allocation are automatically done by the compiler whereas, in heap, it needs to be done by the programmer manually.
3. Handling the Heap frame is costlier than handling the stack frame.
4. Memory shortage problem is more likely to happen in stack whereas the main issue in heap memory is fragmentation.
5. Stack frame access is easier than the heap frame as the stack has a small region of memory and is cache-friendly but in the case of heap frames which are dispersed throughout the memory so it causes more cache misses.
6. A stack is not flexible, the memory size allotted cannot be changed whereas a heap is flexible, and the allotted memory can be altered.
7. Accessing the time of heap takes is more than a stack.

## What is the difference between struct and class?

- Structs are of the value type. They only hold value in memory, while classes are of reference type. It holds a reference of an object in memory.
- Struct memory is stored as stacks while class memory is stored as heaps.

## What is the difference between reference and pointer?

- Value of ref cannot be reassigned while value of pointer can.
- Ref can't hole a null value while pointer can point to null.
- Ref can't work with arrays while pointers can.
- Ref: to access the members of class/struct it uses a '.' | Pointer: uses a '->'
- The memory location of reference can be accessed easily while memory location of pointer have to use a dereference '*'.

## 

# Other

## How would you clear the 7th bit in a 32 bit register?

- Create a mask with the 7th bit set to 0 and all other bits set to 1
- Perform a bitwise AND operation between the register and the mask
- Store the result back in the register

## Describe the concept of object-oriented programming (OOP) and its benefits.

Object-oriented programming aims to implement real-world entities like inheritance, hiding, polymorphism, etc in programming.
- The main aim and benefit of OOP is to bind together the data and the functions that operate on them so that no other part of the code can access this data except that function.
- We can build the programs from standard working modules that communicate with one another, rather than having to start writing the code from scratch which leads to saving of development time and higher productivity.
- It is possible that multiple instances of objects co-exist without any interference

## Explain inheritance

The capability or ability of a class to derive properties and characteristics from another class.