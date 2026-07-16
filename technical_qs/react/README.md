### Why react good?
- Breaks down UI into reusable components, keeps UI in sync with changing data.
- Virtual DOM lightweight in-memory representation of DOM which is used to compare
to DOM and only updates the parts that are different instead of re-rendering everything.

### State and props
- Props: read only passed down from parent to child, can't be modified.
- State is managed by component and updating with setState triggers re-render.

### JSX
Lets you write HTML directly in JS

### React hooks
- Functions that let you use state and other React features without using classes.

### useState
- useState lets a function component hold and update local state.
- Has a setter function that schedules re-render, needs new copy rather than mutating in place.

### useEffect
- useEffect lets you run side effects.
- fetching data, subscribing to events, manually interacting with the DOM - after a component re-renders.
- Takes a function and dependency array, re-runs whenever a value in that array changes.
- Empty array runs it once on mount.
- Can also return cleanup function from it, which runs before effect re-runs or
when the component unmounts, which is useful for things like removing event listeners.

### Component lifecycle
- Mounting (componentDidMount), updating (componentDidUpdate), unmounting (componentWillUnmount)
- With hooks, useEffect can cover all 3.

### What are keys in lists, and why do they matter?
- Keys help React identify which items in a list have changed, been added, or
removed, so it can update the DOM efficiently and correctly rather than re-rendering the whole list.

### Controlled vs uncontrolled components
- Controlled component - input's value comes from state, updates happen through onChange handler.
- Uncontrolled component manages its own state internally in the DOM, and you
access its value via a ref when needed.

### useMemo
- Hook that optimises performance by memoizing the result of expensive calcs,
so they are only recalced when their dependencies change.

### useCallback
- Memoizes a callback function, preventing it from being recreated on every render unless its deps change.

### Fetching data
- Typically inside useEffect with empty dep array, calling fetch and storing result in state.
- Handle loading/error states explicitly so the UI can show spinner or err msg.
- Handle case where component unmounts before fetch resolves, to avoid setting state on an unmounted component.

### Handling forms
- Use controlled inputs tied to state, update state with onChange, handle submit with onSubmit.
