# Amex Python Interview Questions

## Top 3 Detailed Python Questions

### 1. Generators vs Iterators.
**Answer:** Iterators are objects with `__iter__()` and `__next__()` methods. Generators are a simple way to create iterators using `yield` and produce values lazily, one at a time, which saves memory.
**Example:** A generator for Fibonacci values yields each number instead of storing the full sequence.
**Mistake:** Using list comprehensions instead of generator expressions for very large datasets.

### 2. Decorators.
**Answer:** A decorator is a function that takes another function and returns a new function with added behavior.
**Example:** Use decorators for logging, timing, retries, or authentication.
**Mistake:** Forgetting `functools.wraps`, which preserves the wrapped function's metadata.

### 3. Multiprocessing vs Multithreading.
**Answer:** Multithreading is better for I/O-bound work because Python's GIL limits CPU-bound parallelism. Multiprocessing uses separate processes and avoids the GIL, making it suitable for CPU-bound tasks.
**Follow-up:** The GIL is the Global Interpreter Lock that allows only one Python bytecode thread to execute at a time in a single process.
**Mistake:** Using multithreading for CPU-intensive processing expecting linear speedup.

## Rapid-Fire Python Questions with Answers

4. List comprehensions vs `map`/`filter`.
**Answer:** List comprehensions combine looping and conditionals in a concise syntax; `map` and `filter` are functional alternatives that can be more readable for simple transformations.

5. Dictionary internals (Hash tables).
**Answer:** Python dictionaries are hash tables that use keys' hash values for constant-time lookup and handle collisions with open addressing.

6. Deep copy vs Shallow copy.
**Answer:** A shallow copy copies the container structure but not nested objects. A deep copy duplicates nested objects recursively.

7. `*args` and `**kwargs`.
**Answer:** `*args` collects positional arguments into a tuple; `**kwargs` collects keyword arguments into a dict.

8. Mutable vs Immutable types.
**Answer:** Mutable types (list, dict, set) can change in place; immutable types (tuple, str, int) cannot.

9. Lambda functions.
**Answer:** Anonymous inline functions defined with `lambda`; best for short, simple operations.

10. Exception handling (`try/except/finally`).
**Answer:** Use `try` to wrap risky code, `except` to catch errors, and `finally` for cleanup that always runs.

11. Context managers (`with` statement).
**Answer:** Ensure proper setup and teardown of resources, typically using `__enter__` and `__exit__` methods.

12. Magic/Dunder methods (`__init__`, `__str__`).
**Answer:** Special methods let classes support built-in behavior like construction, string conversion, and operator overloads.

13. Class methods vs Static methods.
**Answer:** `@classmethod` receives the class as the first argument; `@staticmethod` receives no implicit first argument.

14. Inheritance and Multiple Inheritance (MRO).
**Answer:** Python resolves method order using the C3 linearization algorithm for multiple inheritance.

15. Set operations (union, intersection).
**Answer:** Use `set.union()`, `set.intersection()`, `|`, and `&` for fast membership and comparison operations.

16. Python memory management and Garbage Collection.
**Answer:** Python uses reference counting plus a cyclic garbage collector for unreachable cycles.

17. `is` vs `==`.
**Answer:** `is` tests identity, `==` tests value equality.

18. `yield from`.
**Answer:** Delegates part of a generator's operations to another generator or iterable.

19. Asyncio basics.
**Answer:** Use `async def`, `await`, and an event loop for asynchronous I/O tasks.

20. File I/O operations.
**Answer:** Use `open()` and context managers for safe reading/writing of files.

21. Pandas: `loc` vs `iloc`.
**Answer:** `loc` selects by labels; `iloc` selects by integer positions.

22. Pandas: Handling missing data.
**Answer:** Use `dropna()`, `fillna()`, or `interpolate()` to manage null values.

23. Virtual environments.
**Answer:** Use `venv`, `virtualenv`, or `conda` to isolate dependencies per project.

24. `__name__ == '__main__'.`
**Answer:** Ensures code runs only when a script is executed directly, not when imported.

25. Time complexity of list/dict operations.
**Answer:** List indexing is O(1), list append is amortized O(1), list search is O(n), dict lookup is O(1) average.

26. Sorting algorithms implementations.
**Answer:** Know Python's Timsort and how to implement common sorts like quicksort or mergesort conceptually.

27. String immutability implications.
**Answer:** Strings cannot be changed in place; operations create new string objects.

28. Closures.
**Answer:** An inner function retains access to variables from an enclosing scope.

29. Type hinting.
**Answer:** Use `typing` annotations like `List[int]`, `Dict[str, Any]`, and `Optional[str]` to document expected types.

30. Unit testing (`pytest`/`unittest`).
**Answer:** Write test functions or classes, assert expected behavior, and automate with a test runner.
