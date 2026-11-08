
Control flow in **GCP Workflows** lets you manage execution paths using conditional branching, loops, and reusable blocks.

---

### 1. Conditional Branching (`switch`, `condition`, `next`)

Decide which step to run next based on data evaluations (like if/else statements).

```yaml
- checkStatus:
    switch:
      - condition: ${status == "active"}
        next: processActive
      - condition: ${status == "pending"}
        next: processPending
    next: defaultStep

```

### 2. Iteration (`for`)

Loop through lists or maps to repeat a task for each item.

```yaml
- loopItems:
    for:
      value: userId
      in: ${["user1", "user2", "user3"]}
      steps:
        - logUser:
            call: sys.log
            args:
              text: ${"Processing " + userId}

```

### 3. Subworkflows & Returning (`return`, `Subworkflows`)

Encapsulate reusable logic into modular functions and exit or return values.

```yaml
main:
  steps:
    - callSub:
        call: calculateSquare
        args:
          x: 5
        result: squareResult
    - finish:
        return: ${squareResult}

subworkflows:
  - calculateSquare:
      params: [x]
      steps:
        - math:
            return: ${x * x}

```

---

> **Summary:** Use `switch` + `condition` + `next` for routing, `for` for looping, `subworkflows` for modularity, and `return` to output results or exit.
---
