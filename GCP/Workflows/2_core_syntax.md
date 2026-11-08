# 📝 Core Syntax: Writing Your First Workflow

## **How Workflows Are Written**

You define workflows using standard text configuration languages:

* **YAML** (Recommended for readability) or **JSON** (Best for programmatic generation).

### **Basic Structure**

Every workflow follows a top-to-bottom layout built around a few essential building blocks:

* **`main`:** The mandatory entry point where your workflow execution always begins.
* **`steps`:** An ordered list of tasks that execute sequentially (one after another).
* **`step names`:** Unique labels assigned to each step so you can reference them, track execution, or jump between them.

---

> 💡 **Example Structure:**
>
> ```yaml
> main:
>   steps:
>     - stepOne:
>         call: http.get
>         args:
>           url: https://api.example.com
>     - stepTwo:
>         return: ${stepOne.body}
>
> ```

## 🔄 Data Passing and Variables in GCP Workflows

Passing data between steps is what turns a list of independent tasks into a smart, dynamic pipeline. Here is how it works:

### **Key Concepts**

* **Expressions (`${...}`):** Everything dynamic in Workflows is wrapped in `${}`. This is how you read variables, evaluate logic, and access previous outputs.
* **Assignment (`assign`):** Used to create, update, or store variables inside a step.
* **Accessing Step Results:** Every step automatically stores its output under its own name. You can grab data from a previous step using `${step_name.body}` or `${step_name.result}`.

---

> 💡 **Quick Example:**
> ```yaml
> main:
>   steps:
>     - getUsername:
>         assign:
>           - userName: "Alex"
>     - greetUser:
>         return: ${"Hello, " + userName + "!"}
> 
> ```
> 
> 

---