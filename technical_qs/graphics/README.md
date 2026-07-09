### Describe the rendering pipeline.

1. **Vertex generation:** Define vertex location, normal, colour, etc.
- Each vertex retrieved from the vertex arrays (as defined by the VAO) is acted upon by a Vertex Shader. Each vertex in the stream is processed in turn into an output vertex.
2. **Vertex transformation/processing:** Rotate, translate, scale, distort
3. **Primitive generation:** Define topology
- The purpose of the primitive assembly step is to convert a vertex stream into a sequence of base primitives.
4. **Primitive processing:** Culling (discarding without rendering), clipping
5. **Rasterisation:** Identify fragments
6. **Fragment processing:** Lights, colour interpolation
- The data for each fragment from the rasterization stage is processed by a fragment shader. The output from a fragment shader is a list of colors for each of the color buffers being written to, a depth value, and a stencil value. Fragment shaders are not able to set the stencil data for a fragment, but they do have control over the color and depth values. 
7. **Pixel operations:** Test fragments and generate pixels, render image to frame buffer


