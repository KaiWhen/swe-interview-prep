### What are the four main pillars of OOP?
Encapsulation, Inheritance, Polymorphism, Abstraction.

### Explain encapsulation.
Encapsulation is the practice of bundling data and the methods
that operate on that data into a single unit, typically a class.
It can restrict direct access to some of the object's internal state using access modifiers like private or protected.
It protects data from unintended interference.

### What is inheritance? Give an example.
A mechanism where a new class (child/subclass) derives properties and behaviors
from an existing class (parent/superclass).
Example: Vehicle as parent, Car and Bike as children inheriting move() method.

### What is polymorphism?
It allows objects to behave differently based on their specific class type i.e. it can take many forms.
It allows the same method name to behave differently based on the object calling it.
Two types:
- Compile‑time (overloading): same method name, different parameters.
- Runtime (overriding): subclass provides specific implementation of a method already defined in its parent.

### What is abstraction? How is it different from encapsulation?
Abstraction is the process of hiding internal implementation details and
showing only essential functionality to the user.
Achieved via abstract classes and interfaces.
Difference: Encapsulation hides data (protects it from outside access);
abstraction hides complexity (shows only what's necessary).

### What is an abstract class (in Java)?
An abstract class is a class that cannot be instantiated and may contain abstract methods
(methods without body) as well as concrete methods (with implementation).
(to put it more simply it's a class where you can't make object instances of it and you
mainly use it for a class to `extend` it)

### What is an interface (in Java)?
An interface is a blueprint for a class that defines a set of methods a class must `implement`.
Modern Java interfaces can contain abstract methods, constants, and also default or static methods with implementations.

### 
