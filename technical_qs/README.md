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