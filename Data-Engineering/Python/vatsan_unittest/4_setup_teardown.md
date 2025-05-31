# Setup & TearDown

### **1. `setUp()`**

* This method is executed before every individual test method within a test case.
* It is commonly used to prepare resources or initialize variables needed for a test.

```python
import unittest

class TestExample(unittest.TestCase):
    def setUp(self):
        self.number = 42
        print("Setup before each test")

    def test_case_1(self):
        self.assertEqual(self.number, 42)

    def test_case_2(self):
        self.assertNotEqual(self.number, 0)
```

### **2. `tearDown()`**

* This method is executed after every individual test method within a test case.
* It is usually employed to clean up resources, such as closing files or database connections.

```python
    def tearDown(self):
        print("Teardown after each test")
```

### **3. `setUpClass()`**

* This is a class-level method that runs **once** before any tests in the test class are executed.
* It's useful for tasks that are expensive and need to be shared across all test methods, such as establishing a database connection.

```python
    @classmethod
    def setUpClass(cls):
        print("Setup before all tests in the class")
```

### **4. `tearDownClass()`**

* This is another class-level method that runs **once** after all tests in the test class have been executed.
* It is used for cleaning up class-level resources created during `setUpClass()`.

```python
    @classmethod
    def tearDownClass(cls):
        print("Teardown after all tests in the class")
```

### **How They Work Together**

The lifecycle of these methods is as follows:

1. **`setUpClass()`** runs first (once, for the entire class).
2. **`setUp()`** runs before each test method.
3. The actual test method runs.
4. **`tearDown()`** runs after each test method.
5. **`tearDownClass()`** runs last (once, for the entire class).

.
