# 📝 Variables in JavaScript: `var`, `let`, and `const`

Variables are containers for storing data. JavaScript has three keywords to declare a variable: `var`, `let`, and `const`. The difference lies mainly in their **scope** (where the variable is accessible) and whether they can be **reassigned** or **redeclared**.

| Feature | `var` | `let` | `const` |
| :--- | :--- | :--- | :--- |
| **Scope** | Function-scoped. | Block-scoped. | Block-scoped. |
| **Reassignable** | Yes. | Yes. | No (must be assigned a value on declaration, and that value cannot change). |
| **Redeclarable** | Yes. | No. | No. |
| **Hoisting** | Initialized with `undefined`. | Initialized without value (causes a "temporal dead zone" error if accessed before declaration). | Initialized without value. |

### Why `let` and `const` replaced `var`

The behavior of `var` (especially its function-scoping and redeclaration ability) often led to bugs and confusion. **Modern JavaScript development strongly prefers `let` and `const`** for better control and predictability.

  * Use `const` by default.
  * Use `let` only if you know the variable's value will change.
  * Avoid using `var`.

-----

## 🔢 Primitive Data Types

A primitive value is data that is not an object and has no methods. They are **immutable**, meaning their value cannot be changed after creation (though the variable holding the primitive can be reassigned).

The main primitive types are:

| Type | Description | Example |
| :--- | :--- | :--- |
| **string** | Textual data, enclosed in single or double quotes, or backticks (template literals). | `'Hello'`, `"World"`, \`Name: ${name}\` |
| **number** | Both integers and floating-point numbers. | `10`, `3.14`, `-5` |
| **boolean** | A logical entity that can only be `true` or `false`. | `true`, `false` |
| **null** | Represents the intentional absence of any object value. It is explicitly set. | `let data = null;` |
| **undefined** | Represents a variable that has been declared but has not yet been assigned a value. | `let x;` |

-----

## 💡 Executable JavaScript Example

You can copy and paste the following code into your browser's developer console (F12) or a Node.js environment to execute it.

```javascript
// --- 1. Variable Declarations (var, let, const) ---

// 1.1. const (Recommended for values that won't change)
// Must be initialized with a value
const PI = 3.14159;
console.log("const PI:", PI);

// ERROR: Cannot reassign a const variable
// PI = 3.0; // Uncommenting this line will throw an error: Assignment to constant variable.

// 1.2. let (Recommended for values that will change)
let counter = 0;
console.log("let counter (initial):", counter);

// Reassignable: OK
counter = counter + 1;
console.log("let counter (reassigned):", counter);

// 1.3. var (Avoid in new code)
var legacyVar = "I am old";
console.log("var legacyVar:", legacyVar);

// Redeclarable (this can lead to bugs with let/const)
var legacyVar = "I am redefined"; // This is valid with var
console.log("var legacyVar (redeclared):", legacyVar);


// --- 2. Primitive Data Types ---

// 2.1. string
let greeting = "Hello, JavaScript!";
console.log("Type of greeting:", typeof greeting); // Output: string

// 2.2. number
let age = 30; // Integer
let price = 19.99; // Float
console.log("Type of age:", typeof age);     // Output: number
console.log("Type of price:", typeof price); // Output: number

// 2.3. boolean
let isStudent = true;
let hasLicense = false;
console.log("Type of isStudent:", typeof isStudent); // Output: boolean

// 2.4. null
let chosenColor = null; // Explicitly no color chosen
console.log("Value of chosenColor:", chosenColor);
// Note: typeof null is a historical JavaScript error that returns 'object'
console.log("Type of chosenColor (typeof null):", typeof chosenColor); // Output: object (a quirk!)

// 2.5. undefined
let address; // Declared but not assigned a value
console.log("Value of address:", address);
console.log("Type of address:", typeof address); // Output: undefined
```