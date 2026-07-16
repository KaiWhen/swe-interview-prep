### What is TypeScript
- TypeScript is a superset of JavaScript that adds static typing
- The main benefit is catching type-related bugs at compile time instead of runtime.
- Especially valuable in larger codebases where it's easy to lose track of what shape data is supposed to have.
- Better autocomplete, inline documentation, and safer refactoring, since your editor knows the types involved

### What are the basic types in TypeScript?
- string, number, boolean, null, undefined, any, unknown, void, arrays
(string[] or Array<string>), tuples (e.g. [string, number]), and object types/interfaces for more complex shapes.

### Difference between interface and type
- `interface` supports declaration merging (you can define the same interface 
twice and it merges the fields), and is generally preferred for defining object 
shapes/contracts, especially with classes (implements).
- `type` is more flexible, it can represent unions, intersections, primitives, 
tuples, and mapped types, not just object shapes.
- use `interface` for object shapes, `type` for anything involving unions or more complex type logic.

### unknown
- accepts any value, but you can't use it until you've narrowed its type (e.g. 
with a type check or type assertion), forcing you to actually verify what it is before operating on it.
- `unknown` is preferred whenever you're not sure of a type up front, like data coming from an API response.

### Union type
- A union type means a value can be one of several types, written like `string | number`.

### Generics
- Generics let you write reusable functions or components that work with 
multiple types while still preserving type safety, instead of using any and losing type information.
```ts
function identity<T>(value: T): T {
  return value;
}
```
- Here `T` is a placeholder type, calling `identity(5)` returns a `number`, calling `identity("hi")` returns a `string`.

### Enums
- fixed set of named constants
```ts
enum Status {
  Active,
  Inactive,
  Pending
}
```
- They're used when a value should only be one of a known, limited set of options.
- alternative: union of string literals `(type Status = "active" | "inactive" | "pending")`
