## **Mocking with `unittest.mock` in Python**

Mocking is a technique used in unit testing where you replace real objects with "mock" objects that simulate the behavior of the real ones. This is useful for testing parts of your code that depend on external resources like databases, APIs, or third-party services without actually calling them.

Python’s `unittest.mock` module provides powerful tools for creating and using mock objects.

---

## **1. Introduction to Mocking**

Mocking is helpful when:

* You need to **test code that interacts with an external service** (e.g., APIs, databases).
* You want to **control dependencies** to isolate the component being tested.
* You want to **test edge cases** without affecting actual data.
* You need to **simulate errors or specific return values** for better test coverage.

Example:

Suppose we have a function that fetches data from an API. Instead of making actual API calls during testing, we can replace the API call with a mock that returns predefined data.

---

## **2. The `Mock` Class**

The `Mock` class allows you to create mock objects that behave like real objects. You can configure them to return specific values and track interactions.

### **Basic Example of `Mock`**

```python
from unittest.mock import Mock

# Create a mock object
mock_obj = Mock()

# Set a return value for a method call
mock_obj.some_method.return_value = "Hello, Mock!"

# Calling the mock method
print(mock_obj.some_method())  # Output: Hello, Mock!

# Checking if the method was called
mock_obj.some_method.assert_called()
```

### **Key Features of `Mock`**

* **Set return values:** `.return_value`
* **Simulate exceptions:** `.side_effect`
* **Track calls:** `.called`, `.call_count`
* **Assert calls:** `.assert_called()`, `.assert_called_once_with(...)`

---

## **3. Using `patch` for Mocking**

The `patch` decorator/context manager is used to temporarily replace an object during testing.

### **Example: Mocking a function with `patch`**

Let's say we have a function that fetches data from a web service.

```python
import requests

def get_weather(city):
    response = requests.get(f"https://api.weather.com/{city}")
    return response.json()
```

During testing, we don’t want to make real API calls. We can use `patch` to mock `requests.get`.

```python
from unittest.mock import patch

@patch("requests.get")
def test_get_weather(mock_get):
    # Define mock return value
    mock_get.return_value.json.return_value = {"temp": 25, "weather": "Sunny"}

    # Call the function
    result = get_weather("Chennai")

    # Assertions
    assert result["temp"] == 25
    assert result["weather"] == "Sunny"
    mock_get.assert_called_once_with("https://api.weather.com/Chennai")

test_get_weather()
```

### **How `patch` Works**

* **`patch("requests.get")`** replaces `requests.get` with a mock during the test.
* The mock is passed as an argument (`mock_get`).
* We set the `.return_value.json.return_value` to return a fake API response.
* We then assert that `requests.get` was called with the expected URL.

---

## **4. Common Use Cases**

### **1. Mocking Class Methods**

If a class method interacts with a database or external service, we can mock it.

```python
from unittest.mock import patch

class Database:
    def get_data(self):
        return "Real Data"

@patch.object(Database, "get_data", return_value="Mock Data")
def test_database(mock_method):
    db = Database()
    assert db.get_data() == "Mock Data"

test_database()
```

### **2. Mocking a Built-in Function (`open`)**

If you have code that reads from a file, you can mock `open()`.

```python
from unittest.mock import mock_open, patch

@patch("builtins.open", new_callable=mock_open, read_data="Mock File Content")
def test_read_file(mock_file):
    with open("dummy.txt") as f:
        content = f.read()
    assert content == "Mock File Content"

test_read_file()
```

### **3. Simulating Exceptions**

You can use `.side_effect` to simulate exceptions.

```python
mock_obj.some_method.side_effect = ValueError("An error occurred")
try:
    mock_obj.some_method()
except ValueError as e:
    print(e)  # Output: An error occurred
```

---

## **Conclusion**

* `Mock` helps replace real objects in tests.
* `patch` temporarily replaces objects (functions, methods, classes).
* Mocking is useful for testing code that depends on databases, APIs, or other services.

.
