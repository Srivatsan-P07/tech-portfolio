# Assertions

**1. Creating Simple Test Cases with Assertions:**
Assertions are used to check if a certain condition is true. If the condition is false, the test fails. Here's an example:

```python
import unittest

class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # Check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
```
---

### Example Breakdown

- **Importing `unittest`:** This module provides the necessary classes and functions for creating and running tests.
- **Creating a Test Class:** `TestStringMethods` is a subclass of `unittest.TestCase`.
- **Defining Test Methods:**
  - `test_upper`: Checks if the `upper()` method converts a string to uppercase.
  - `test_isupper`: Uses `assertTrue` and `assertFalse` to check if a string is uppercase.
  - `test_split`: Checks if the `split()` method splits a string correctly and raises a `TypeError` when the separator is not a string.
- **Running Tests:** `unittest.main()` discovers and runs all test methods in the `TestStringMethods` class.

---

### Common Assertions

- `assertEqual(a, b)`: Check if `a` equals `b`.
- `assertTrue(x)`: Check if `x` is `True`.
- `assertFalse(x)`: Check if `x` is `False`.
- `assertRaises(exc, fun, *args, **kwds)`: Check if `fun(*args, **kwds)` raises an exception `exc`.