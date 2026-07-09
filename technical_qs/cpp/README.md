### What are references in C++?
When a variable is described as a reference it becomes an alias of the already existing variable.
They refer to the same memory location.

Syntax:
```cpp
int foo = 10;
int& ref = foo;
```

### What are pointers?
A variable that stores the memory address of another variable.

```cpp
int var = 10;
int *ptr = &var;
printf("%p", ptr); // directly access pointer
printf("%d", *ptr); // dereference pointer
```

### Explain the differences between a pointer and a reference.
Key differentiators include that a reference must always be initialized and can't be reassigned,
while a pointer can be nullptr and changed. A reference also doesn't require explicit dereferencing.

### What is the difference between new/delete?
The difference is that `new` calls the object's constructor, and `delete` calls its destructor,
making them mandatory for C++ objects.

### What is the difference between a shallow copy and a deep copy?
- A shallow copy copies the pointer's address, causing two pointers to share the same memory.
- A deep copy creates a new allocation and copies the contents, ensuring each object has its own independent resource.
Deep copies prevent issues like double deletion.

### When is a copy constructor called?
A copy constructor in C++ is a special constructor that initializes a new object as a copy of an existing object.
- When an object is passed by value.
- When an object is returned by value from a function.
- When one object is initialized directly using another (e.g., Class obj2 = obj1;).

### Explain the concept of virtual functions and the v-table.
A virtual function enables runtime polymorphism. The vtable is a lookup table of function pointers
maintained by the compiler; each class with a virtual function has one, and each object has a pointer to it (vptr).

### Virtual Funtions
- A virtual function is a member function that is declared within a base class using the keyword virtual
and is re-defined (Overridden) in the derived class.
- Virtual functions are mainly related to inheritance,
allowing derived classes to provide their own implementation of base class functions.
- When a derived class object is deleted through a base class pointer, a virtual destructor in the
base class ensures that both the derived and base class destructors are called, safely releasing all resources.

```cpp
class Shape
{
  public:
  
    // Virtual function
    virtual void calculate()
    {
        cout << "Area of your Shape ";
    }

    // Virtual destructor
    virtual ~Shape()
    {
        cout << "Shape Destructor called\n";
    }
};

// Derived class: Rectangle
class Rectangle : public Shape
{
  public:
    int width, height, area;

    void calculate() override
    {
        width = 5;
        height = 10;

        area = height * width;
        cout << "Area of Rectangle: " << area << "\n";
    }

    ~Rectangle()
    {
        cout << "Rectangle Destructor called\n";
    }
};
```

#### Pure Virtual Functions
- A pure virtual function is a function in a base class with = 0 and no body,
which must be overridden in derived classes.
- A class with at least one pure virtual function is abstract and cannot be instantiated, only used as an interface.
- A pure virtual destructor is a destructor in a base class declared with = 0.
It makes the class abstract and ensures that when you delete a derived class object through a base class pointer,
the derived destructor runs first, followed by the base destructor, cleaning up everything properly.

Define pure virtual destructor outside of class like so:
```cpp
Base::~Base()
{
    cout << "Base destructor called" << endl;
}
```

#### Early and Late Binding
When a function is called in the code, binding decides which function gets executed based on the context such as the
type of object or the function signature. 
- **Early Binding:** Function call resolved during compilation, faster. Happens with non-virtual functions.
- **Late Binding:** Function call decided at runtime, slower. Happens with virtual functions.

### What is object slicing?
Object slicing occurs when a derived class object is assigned to a base class object by value,
"slicing off" the derived part and losing its specific behaviors. This is avoided by using pointers or references.

### 
