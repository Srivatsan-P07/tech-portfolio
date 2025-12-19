# 1. Function Declarations vs. Expressions

The main difference between these two is **hoisting**—the ability to call a function before it appears in your code.

### Function Declaration

A declaration defines a named function. These are hoisted, meaning you can call them at the top of your script even if the definition is at the bottom.

```javascript
greet(); // Works! Result: "Hello!"

function greet() {
  console.log("Hello!");
}

```

### Function Expression

An expression involves storing a function inside a variable. These are **not** hoisted; you must define them before you use them.

```javascript
// This would cause an error if called before this line
const speak = function() {
  console.log("I am an expression.");
};

speak(); 

```

# 2. Scope: Local vs. Global

Scope determines where your variables are accessible.

* **Global Scope:** Variables defined outside of any function. They can be accessed from anywhere.
* **Local (Function) Scope:** Variables defined inside a function. They are "invisible" to the rest of the program.

```javascript
let globalVar = "I am everywhere";

function scopeTest() {
  let localVar = "I am hidden";
  console.log(globalVar); // Accessible
  console.log(localVar);  // Accessible
}

scopeTest();
console.log(localVar); // ReferenceError: localVar is not defined

```



# 3. Parameters and Return Values

Think of a function like a machine: **Parameters** are the raw materials you put in, and the **Return Value** is the finished product that comes out.

* **Parameters:** Placeholders defined in the function signature.
* **Arguments:** The actual values you pass when calling the function.
* **Return:** The keyword that stops the function and sends a value back to the caller.

```javascript
function multiply(a, b) { // a and b are parameters
  return a * b;           // the result is sent back
}

let result = multiply(5, 4); // 5 and 4 are arguments
console.log(result); // 20

```



# 4. Arrow Functions (`=>`)

Introduced in ES6, arrow functions provide a shorter syntax. They are always anonymous (meaning you usually assign them to a variable).

**Key features:**

* Shorter syntax.
* Implicit return (if it's a single line, you don't need the `return` keyword).
* They do not have their own `this` context (great for callbacks).

```javascript
// Standard Expression
const add = function(x, y) {
  return x + y;
};

// Arrow Function
const addArrow = (x, y) => x + y; 

console.log(addArrow(10, 2)); // 12

```


---

### Summary Table

| Feature | Declaration | Expression | Arrow Function |
| --- | --- | --- | --- |
| **Hoisted?** | Yes | No | No |
| **Syntax** | `function name() {}` | `const name = function() {}` | `const name = () => {}` |
| **Best Use** | General purpose | Callbacks/Closures | Short logic / Callbacks |