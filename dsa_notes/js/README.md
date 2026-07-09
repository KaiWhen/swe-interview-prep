### Creating arrays
```js
const arr = [1, 2, 3];
new Array(5).fill(0);        // [0,0,0,0,0]
Array.from({length: 5}, (_, i) => i); // [0,1,2,3,4]
```

### Adding/removing in arrays
```js
arr.push(x);      // add to end
arr.pop();        // remove from end
arr.unshift(x);   // add to start
arr.shift();      // remove from start
arr.splice(start, deleteCount, ...items); // insert/remove anywhere
```

### Iterating/transforming
```js
arr.map(x => x * 2);         // makes a new array with all elements *2
arr.filter(x => x > 2);
arr.reduce((acc, x) => acc + x, 0); // reduce array to one number, starting from value of 0 (this gets sum)
arr.forEach(x => console.log(x));
arr.find(x => x > 2);        // first match, or undefined
arr.findIndex(x => x > 2);   // index of first match, or -1
arr.some(x => x > 2);        // true if any match
arr.every(x => x > 2);       // true if all match
arr.includes(x);             // boolean
arr.indexOf(x);               // index or -1
```

### Sorting/ordering
```js
arr.sort((a, b) => a - b);   // ascending numbers — ALWAYS pass a comparator for numbers
arr.sort((a, b) => b - a);   // descending
arr.sort((a, b) => a.name.localeCompare(b.name)) // alphabetical orders
arr.reverse();
```

### Slicing/combining
```js
arr.slice(start, end);   // non-mutating copy of a range
arr.concat(otherArr);    // or [...arr, ...otherArr]
arr.join(', ');           // array -> string
```

### Destructuring/spread
```js
const [first, second, ...rest] = arr;
const combined = [...arr1, ...arr2];
```

### Strings
```js
str.split('');            // string -> array of chars
str.split(' ');            // split on space
arr.join('');               // array -> string
str.toLowerCase() / str.toUpperCase();
str.trim();                 // removes whitespace from both sides
str.includes('sub');
str.indexOf('sub');
str.slice(start, end);      // substring (supports negative indices)
str.substring(start, end);  // similar, no negative indices
str.replace('a', 'b');      // first match only
str.replaceAll('a', 'b');
str.padStart(n, '0') / str.padEnd(n, '0');   // pad start/end of str with 0 until it's length n
str.charAt(i) / str[i];
str.charCodeAt(i);          // char -> ASCII code (useful for letter math)
String.fromCharCode(code);  // ASCII code -> char
[...str];                    // spread string into array of characters (handles unicode better than split(''))
```

### Reverse a string
```js
str.split('').reverse().join('');
```

### Objects
```js
const obj = { a: 1, b: 2 };
Object.keys(obj);      // ['a', 'b']
Object.values(obj);    // [1, 2]
Object.entries(obj);   // [['a',1], ['b',2]]
Object.assign({}, obj, { c: 3 }); // merge (or use spread)
const merged = { ...obj, c: 3 };
obj.hasOwnProperty('a'); // or: 'a' in obj
delete obj.a;

// iterate
for (const key in obj) { ... }
for (const [key, value] of Object.entries(obj)) { ... }
```

### Map (better than object when you need guaranteed order, non-string keys, or frequent add/delete)
```js
const map = new Map();
map.set('a', 1);
map.get('a');          // 1
map.has('a');          // true
map.delete('a');
map.size;
for (const [key, value] of map) { ... }
```

### Set (unique values, fast lookup)
```js
const set = new Set([1, 2, 2, 3]);   // {1, 2, 3} — dedupes automatically
set.add(4);
set.has(2);      // true
set.delete(2);
set.size;
[...set];         // back to array
```

### Stack/Queue
```js
// Stack (LIFO) — use push/pop
stack.push(x);
stack.pop();

// Queue (FIFO) — use push/shift (shift is O(n), fine for small inputs)
queue.push(x);
queue.shift();
```

### Maths
```js
Math.max(...arr);
Math.min(...arr);
Math.floor(x) / Math.ceil(x) / Math.round(x);
Math.abs(x);
Math.pow(x, y);   // or x ** y
Number.isInteger(x);
parseInt(str, 10);
parseFloat(str);
```

### Freq counting
```js
const counts = {};
for (const x of arr) counts[x] = (counts[x] || 0) + 1;
```

### Two pointer (two-sum sorted) Working with sorted arrays, linked lists, or problems involving sums/subarrays.
```js
const twoSumSorted = (nums, target) => {
    let left = 0, right = nums.length - 1;

    while (left < right) {
        let sum = nums[left] + nums[right];

        if (sum === target) return [left, right];
        sum < target ? left++ : right--;
    }

    return [];
};
```

### Sliding window / Finding maximum/minimum/longest subarrays.
Longest substring without repeating chars
```js
const lengthOfLongestSubstring = (s) => {
    let set = new Set();
    let left = 0, maxLength = 0;

    for (let right = 0; right < s.length; right++) {
        while (set.has(s[right])) {
            set.delete(s[left]);
            left++;
        }
        set.add(s[right]);
        maxLength = Math.max(maxLength, right - left + 1);
    }

    return maxLength;
};
```

### Binary search
```js
const binarySearch = (array) => {
  const condition = (value) => {
    // define your condition here
  }

  let left = 0;
  let right = array.length;

  while (left < right) {
    const mid = left + Math.floor((right - left) / 2);
    if (condition(mid)) {
      right = mid;
    } else {
      left = mid + 1;
    }
  }
  return left;
}
```
