### Managing Data in GCP Workflows

Data management in GCP Workflows relies on three core concepts: storing state with **variables**, computing dynamic values with **expressions**, and utilizing supported **data types**.

---

### Core Concepts

* **`assign` Step:** Used to declare, initialize, or update variables as your workflow progresses.
* **Expressions (`${...}`):** Enclosed in dollar signs and curly braces, expressions let you evaluate values, perform calculations, access object properties, or manipulate strings dynamically.
* **Data Types:** GCP Workflows natively supports JSON-compatible types:
* `String`, `Int`, `Boolean`, `Null`
* `Map` (key-value pairs)
* `List` (ordered arrays)



---

### Quick Example

```yaml
- init:
    assign:
      - workflow_name: "OrderProcessor" # String
      - retry_count: 3                 # Int
      - is_active: true                # Boolean
      - item_list: ["apple", "banana"] # List
      - user_data:                     # Map
          id: 101
          status: "pending"
- calculate:
    assign:
      - next_retry: ${retry_count + 1}
      - first_item: ${item_list[0]}

```
---