# 1. Operators

Operators allow you to perform actions on variables and values.

### Arithmetic Operators

Used for mathematical calculations.

* **`+` (Addition):** Adds numbers or concatenates strings.
* **`-` (Subtraction):** Subtracts numbers.
* **`*` (Multiplication):** Multiplies numbers.
* **`/` (Division):** Divides numbers.
* **`%` (Modulus):** Returns the division remainder (e.g., `5 % 2` is `1`).
* **`**` (Exponentiation):** Raises to a power (e.g., `2 ** 3` is `8`).

### Comparison Operators

Used to compare two values, returning a **Boolean** (`true` or `false`).

* **`==` vs `===`:** Always prefer `===` (Strict Equality). It checks both the **value** and the **type**.
* **`!=` vs `!==`:** Strict inequality.
* **`>` / `<`:** Greater than / Less than.
* **`>=` / `<=`:** Greater than or equal to / Less than or equal to.

### Logical Operators

Used to combine multiple boolean expressions.

* **`&&` (AND):** Returns `true` only if **both** sides are true.
* **`||` (OR):** Returns `true` if **at least one** side is true.
* **`!` (NOT):** Reverses the boolean (true becomes false).

```javascript
let score = 10;
let passes = score > 5 && score < 20; // true

```

---

# 2. Conditional Statements

Conditionals allow your code to take different paths based on different inputs.

### If / Else If / Else

The most common way to branch logic.

```javascript
let hour = 14;

if (hour < 12) {
  console.log("Good morning");
} else if (hour < 18) {
  console.log("Good afternoon"); // This will run
} else {
  console.log("Good evening");
}

```

### Switch Statement

Best used when you have a single variable and many specific "cases" it could match. It's often cleaner than a long chain of `if/else`.

```javascript
let day = "Monday";

switch (day) {
  case "Monday":
    console.log("Start of the work week!");
    break; // Stops the execution from falling into the next case
  case "Friday":
    console.log("Weekend is near!");
    break;
  default:
    console.log("Just a regular day.");
}

```

---

# 3. The Ternary Operator

The ternary operator is a shorthand for an `if...else` statement. It is the only JavaScript operator that takes three operands.

**Syntax:** `condition ? valueIfTrue : valueIfFalse`

```javascript
let age = 20;

// Traditional If/Else
let status;
if (age >= 18) {
  status = "Adult";
} else {
  status = "Minor";
}

// Ternary equivalent (One line!)
let statusTernary = age >= 18 ? "Adult" : "Minor";

console.log(statusTernary); // "Adult"

```

---

### Summary Table

| Concept | Purpose | Key Symbols |
| --- | --- | --- |
| **Arithmetic** | Math | `+`, `-`, `*`, `/`, `%` |
| **Comparison** | Checking equality/size | `===`, `!==`, `>`, `<` |
| **Logical** | Combining conditions | `&&`, ` |
| **If/Else** | Flexible branching | `if`, `else if`, `else` |
| **Switch** | Fixed-value branching | `switch`, `case`, `default` |
| **Ternary** | Simple 1-line decisions | `? :` |
