# Production-Ready Python Code Checklist

## 1. Single Responsibility Functions
Each function should perform one well-defined task. Avoid combining loading, validation, transformation, and output in a single function.

**❌ Poor**
```python
def process_data():
    # Load CSV
    # Validate data
    # Transform data
    # Save output
```

**✅ Better**
```python
def load_data():
    ...

def validate_data():
    ...

def transform_data():
    ...

def save_data():
    ...
```

---

## 2. Descriptive Naming
Use variable and function names that clearly describe their purpose. Someone reading the code should understand what each value represents.

**❌ Poor**
```python
df = pd.read_csv(file)
x = df.groupby("symbol")["close"].mean()
```

**✅ Better**
```python
price_data = pd.read_csv(file)

average_price_by_symbol = (
    price_data.groupby("symbol")["close"]
    .mean()
)
```

---

## 3. Testable Functions
Write functions that can be tested independently without relying on external state or side effects.

**❌ Poor**
```python
def process():
    df = pd.read_csv("prices.csv")
    ...
```

**✅ Better**
```python
def calculate_average_price(df):
    return df.groupby("symbol")["close"].mean()
```

---

## 4. Validate Inputs Early
Validate inputs before processing to fail fast and provide meaningful error messages.

**❌ Poor**
```python
df.groupby("symbol")["close"].mean()
```

**✅ Better**
```python
required_columns = {"symbol", "close"}

missing = required_columns - set(df.columns)

if missing:
    raise ValueError(f"Missing columns: {missing}")
```

---

## 5. Use Type Hints
Type hints improve readability, IDE support, and static analysis.

**❌ Poor**
```python
def aggregate(df):
    ...
```

**✅ Better**
```python
import pandas as pd

def aggregate(df: pd.DataFrame) -> dict[str, float]:
    ...
```

---

## 6. Write Docstrings
Document what a function does, its inputs, outputs, and any important behavior.

**❌ Poor**
```python
def aggregate(df):
    ...
```

**✅ Better**
```python
def aggregate(df: pd.DataFrame) -> dict[str, float]:
    """Calculate the average closing price for each stock symbol."""
```

---

## 7. Replace Magic Values with Constants
Avoid hardcoding numbers and strings throughout the code. Define them once as named constants.

**❌ Poor**
```python
if retries > 3:
    ...

df = df.fillna(0)
```

**✅ Better**
```python
MAX_RETRIES = 3
DEFAULT_PRICE = 0

if retries > MAX_RETRIES:
    ...

df = df.fillna(DEFAULT_PRICE)
```

---

## 8. Design for Extensibility
Structure code so that new features can be added with minimal changes.

**❌ Poor**
```python
def aggregate(df):
    return df.groupby("symbol")["close"].mean()
```

**✅ Better**
```python
def aggregate(df, metric="mean"):
    grouped = df.groupby("symbol")["close"]

    if metric == "mean":
        return grouped.mean()

    if metric == "median":
        return grouped.median()

    raise ValueError("Unsupported metric")
```

---

## 9. Avoid Code Duplication (DRY)
Don't repeat the same logic in multiple places. Extract reusable code into functions.

**❌ Poor**
```python
df1 = pd.read_csv(file1)
df1.columns = df1.columns.str.lower()

df2 = pd.read_csv(file2)
df2.columns = df2.columns.str.lower()
```

**✅ Better**
```python
def load_csv(file_path):
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.lower()
    return df
```

---

## 10. Handle Exceptions Gracefully
Catch expected exceptions and provide meaningful messages instead of allowing cryptic errors.

**❌ Poor**
```python
df = pd.read_csv(file_path)
```

**✅ Better**
```python
try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    raise FileNotFoundError(f"Input file '{file_path}' was not found.")
```

---

## 11. Keep Functions Small
Aim for short functions that are easy to understand at a glance. Long functions usually indicate multiple responsibilities.

**❌ Poor**
```python
def process_everything():
    # 200 lines of code
```

**✅ Better**
```python
def load():
    ...

def clean():
    ...

def aggregate():
    ...

def export():
    ...
```

---

## 12. Separate Business Logic from I/O
Keep data processing separate from reading files, writing files, databases, or APIs.

**❌ Poor**
```python
def process():
    df = pd.read_csv("prices.csv")
    return df.groupby("symbol")["close"].mean()
```

**✅ Better**
```python
def calculate_average_price(df):
    return df.groupby("symbol")["close"].mean()

df = pd.read_csv("prices.csv")
result = calculate_average_price(df)
```