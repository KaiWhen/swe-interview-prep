### Event Loop

- Enables asynchronous programming
- Since JavaScript is single-threaded, it uses the event loop to handle multiple tasks without blocking the main thread
- The event loop continuously checks whether the call stack is empty and whether there are pending tasks in the callback queue or microtask queue.
- Call Stack: JavaScript has a call stack where function execution is managed in a Last-In, First-Out (LIFO) order.
- Web APIs (or Background Tasks): These include setTimeout, setInterval, fetch, DOM events, and other non-blocking operations.
- Callback Queue (Task Queue): When an asynchronous operation is completed, its callback is pushed into the task queue.
- Microtask Queue: Promises and other microtasks go into the microtask queue, which is processed before the task queue.

![eventloop](image.png)
<br>
[source: GeeksForGeeks](https://www.geeksforgeeks.org/javascript/what-is-an-event-loop-in-javascript/)

### Closure

- When a function remembers the environment in which it was created, even after the environment has finished executing.
![closure-example](image-1.png)

### Hoisting

- Moves var declarations to the top of the scope, so you can use them before they are declared.
- let/const variables get a ReferenceError when used before declared.
- function declarations are usable before declaration, function expressions are not (const hello = function...)

###
