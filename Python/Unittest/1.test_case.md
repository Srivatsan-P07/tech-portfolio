# Getting Started with `unittest`

**1. Basic Structure of a Test Case:**
A test case is a single unit of testing. It checks for a specific response to a particular set of inputs. Here's a simple example:

```python
import unittest

class TestMathOperations(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(1 + 1, 2)

if __name__ == '__main__':
    unittest.main()
```

**2. `unittest.TestCase`:**
- `unittest.TestCase` is a base class provided by the `unittest` module.
- You create test cases by subclassing `unittest.TestCase`.
- Each method in the subclass represents a single test.

**3. Running Tests:**
- You can run tests using the command line or within a script.
- When you call `unittest.main()`, it runs all the test methods in the `TestMathOperations` class.

### Example Breakdown

- **Importing `unittest`:** This module provides classes and functions for creating and running tests.
- **Creating a Test Class:** `TestMathOperations` is a subclass of `unittest.TestCase`.
- **Defining Test Methods:** `test_addition` is a method that checks if `1 + 1` equals `2`.
- **Running Tests:** `unittest.main()` discovers and runs all test methods.