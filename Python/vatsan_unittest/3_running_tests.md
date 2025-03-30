# Unittesting Runner

### 1. **Running Tests via CLI**

* You can execute Python unit tests directly from the command line by navigating to the directory containing your test files.
* Use the following command:
  ```bash
  python -m unittest discover
  ```
* This will automatically discover and execute all test cases in the current directory and its subdirectories.

### 2. **How Test Discovery Works in `unittest`**

* Test discovery looks for:
  * Files named `test*.py` by default (e.g., `test_example.py`).
  * Test classes derived from `unittest.TestCase`.
  * Methods within those classes that start with the prefix `test`.

### 3. **Customizing Test Discovery**

* You can specify a directory, pattern, or module for test discovery:

  ```bash
  python -m unittest discover -s <directory> -p <pattern> -t <top_level_directory>
  ```

  * `-s`: Start directory (where to look for tests).
  * `-p`: Pattern (e.g., `test_*.py` to match specific files).
  * `-t`: Top-level directory (optional, for relative imports).

### 4. **Example Structure for Test Discovery**

Suppose you have the following file structure:

```
my_project/
├── module1.py
├── tests/
│   ├── test_module1.py
│   ├── test_module2.py
```

From the `my_project` directory, run:

```bash
python -m unittest discover -s tests -p "test_*.py"
```

### 5. **Running Specific Tests**

* You can execute individual tests by specifying the test file or test case:
  ```bash
  python -m unittest tests.test_module1
  ```

### Summary

Using `unittest` and CLI for test discovery is efficient for locating and executing tests systematically. These tools follow established naming conventions and directory structures, making it easier to manage and debug test cases.

.
