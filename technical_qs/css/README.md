### Explain the box model
Every element is made up of four layers, from inside out:
- content (the actual text/image)
- padding (space between content and border)
- border (the edge around padding)
- margin (space outside the border, between this element and others).
- By default, width/height only apply to the content box, so padding and border add to the total rendered size
- unless you use `box-sizing: border-box`, which makes width/height include padding and border,
making sizing much more predictable.

### Difference between position: static, relative, absolute, fixed, and sticky
- static is the default, normal document flow, no positioning applied.
- relative positioning allows an element to be positioned relative to its normal position in the document flow.
    - By using the `top`, `right`, `bottom`, and `left` properties,
    you can adjust its position without affecting the layout of other elements.
- absolute: adjusts an element's position relative to its parent.
If no parent element is present, the document body is used as the parent.
Removes from the normal document flow.
- fixed: relative to the viewport and stays in place even when scrolling.
- sticky: behaves like relative until scrolled to a certain point, used for headers to stick to top.

### Flexbox vs Grid
- Flexbox: 1D, lays items out along a single row or col and is good for navbars, button groups, centering content.
- Grid: 2D, lets you control rows and cols, good for full page layouts and more complex structures.

