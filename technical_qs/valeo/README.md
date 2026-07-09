### Neural Rendering
A field combining deep learning with computer graphics to generate images and video from 2D or 3D data.
Unlike traditional methods, it uses neural networks to learn and control scene properties like lighting,
camera position, and geometry.
Could contrast this with traditional rendering, or simply state:
"It's like teaching a neural network to understand the physics of light in a scene to create new, photorealistic views."

### OpenGL ES vs. Vulkan:
Both are low-level APIs for programming GPUs, but they have key differences.
The main interview point is that Vulkan is newer, more explicit and offers better performance and
control for complex applications but requires more code and expertise.

### What is OpenGL ES?
OpenGL ES (Open Graphics Library for Embedded Systems) is a streamlined version of the
OpenGL API designed for mobile and embedded devices. 

### What is Vulkan?
Vulkan is a cross-platform API and open standard for 3D graphics and parallelized computing.
It was intended to address the shortcomings of OpenGL, and allow developers more control over the GPU.
Vulkan is intended to offer higher performance and more efficient CPU and GPU usage
compared to the older OpenGL and Direct3D 11 APIs, by providing a considerably lower-level API that
more closely resembles how modern GPUs work.

### Generative Models (NeRF & 3DGS)
- **NeRF (Neural Radiance Fields):** are a method for creating 3D representations of scenes from 2D images,
allowing for photorealistic view synthesis.
Works by training a neural network to map 3D coordinates to color and density,
allowing it to synthesize new views of a scene.
- **3DGS (3D Gaussian Splatting):** real time radiance field rendering. 
Represents a scene as millions of overlapping blobs (Gaussians)
and is known for its real-time rendering speed while maintaining high visual quality.

NeRF offers higher potential quality but is slower to render, whereas 3DGS is very fast for interactive applications.

### SW Unit Testing
**Unit Testing / Software (SW) Unit Test Specification:**
A method for verifying the smallest testable parts of an application, such as a single function or method, in isolation.
A Software (SW) Unit Test Specification is the formal document that
defines the conditions, inputs,and expected results for each unit test.

### Module Specification/Test
**Module Specification / Module Test:** A 'module' is a larger component of software that performs a specific function,
grouping several units together. The Module Specification is the blueprint for this component,
while the Module Test verifies the functionality of the complete module,
often checking how its different internal units interact.

### Software Requirements Specification (SRS) & High Level Design (HLD)
An SRS is a document that details what a software system should do—its capabilities, constraints, and features.
In contrast, the High Level Design (HLD) outlines how the system will achieve those requirements,
describing the overall system architecture, its major components, and how they fit together.

### SMATA
Seems to be Valeo's internal data logging tool for their advanced driver-assistance systems (ADAS).
It's used to record data from vehicle sensors (cameras, LiDAR, radar) to train and validate AI models.

### Configuration Management (CM) Database
In software, a version control system (like Git) serves as the Configuration Management database.
This is a controlled repository that stores all project artifacts—source code, design documents,
test specifications, and unit tests.

### Artefacts
Any and all work products created during the development lifecycle.
This includes source code, design and test documents, scripts, data files, training results, and meeting notes.

### ADAS
Advanced Driving Assistance Systems (ADAS) refers to active and passive safety systems aiming at preventing or
minimizing car accidents on the road, mainly caused by human error.