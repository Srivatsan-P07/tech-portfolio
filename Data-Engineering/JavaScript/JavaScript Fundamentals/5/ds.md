In JavaScript, **Data Structures** are simply ways to organize and store data so that we can use it efficiently. The two most common structures you'll use daily are **Arrays** and **Objects**.

---

## 1. Arrays

An array is an ordered list of values. Think of it like a numbered shelf where each item has a specific position (index), starting from **0**.

### Basic Methods

* **`push()`**: Adds an item to the **end** of the array.
* **`pop()`**: Removes the **last** item from the array.

```javascript
let fruits = ['apple', 'banana'];

fruits.push('cherry'); // ['apple', 'banana', 'cherry']
fruits.pop();         // ['apple', 'banana']

```

### Advanced Methods (Functional)

These methods are powerful because they don't change the original array; they create a new one.

* **`map()`**: Transforms every item in the array.
* **`filter()`**: Keeps only the items that meet a certain condition.

```javascript
const numbers = [1, 2, 3, 4];

// Double every number
const doubled = numbers.map(num => num * 2); 
// Output: [2, 4, 6, 8]

// Keep only numbers greater than 2
const bigNumbers = numbers.filter(num => num > 2); 
// Output: [3, 4]

```

---

## 2. Objects

While arrays are ordered lists, **Objects** are collections of **key-value pairs**. They are used to represent "things" with properties (like a person, a car, or a user profile).

```javascript
const user = {
    name: 'Alex',
    age: 25,
    'home town': 'New York'
};

```

### Accessing Data: Dot vs. Bracket Notation

There are two ways to get data out of an object:

| Feature | **Dot Notation** (`obj.key`) | **Bracket Notation** (`obj['key']`) |
| --- | --- | --- |
| **Readability** | Clean and easy to read. | A bit more cluttered. |
| **Variables** | Cannot use variables. | **Can** use variables to access keys. |
| **Special Chars** | Cannot have spaces or symbols. | **Can** handle spaces and special characters. |

#### Examples:

```javascript
// 1. Dot Notation (The Standard)
console.log(user.name); // 'Alex'

// 2. Bracket Notation (The Flexible)
// Required for keys with spaces:
console.log(user['home town']); // 'New York'

// Required when using a variable:
const query = 'age';
console.log(user[query]); // 25

```

---

## When to use which?

* Use an **Array** when the **order** of items matters (e.g., a list of messages, a queue).
* Use an **Object** when you want to describe a single entity with different **properties** (e.g., a product with a name, price, and description).