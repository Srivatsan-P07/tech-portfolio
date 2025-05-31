### **DAGs (Directed Acyclic Graphs) in Apache Airflow**

A DAG in Apache Airflow represents a **workflow** as a collection of tasks with defined dependencies and execution order. It ensures that workflows are executed in a logical sequence without any circular dependencies.

---

#### **Structure**

* A DAG is defined in Python code and consists of:
  * **Tasks** : Individual units of work (e.g., data extraction, transformation, or loading).
  * **Dependencies** : Relationships between tasks that dictate the execution order.
* Example of a simple DAG structure:
  ```python
  from airflow import DAG
  from airflow.operators.dummy import DummyOperator
  from datetime import datetime

  with DAG('example_dag', start_date=datetime(2023, 1, 1), schedule_interval='@daily') as dag:
      task1 = DummyOperator(task_id='start')
      task2 = DummyOperator(task_id='process')
      task3 = DummyOperator(task_id='end')

      task1 >> task2 >> task3  # Defining dependencies
  ```

---

#### **Scheduling**

* DAGs are scheduled to run at specific intervals using the `schedule_interval` parameter.
* Common scheduling options:
  * `@daily`: Runs once a day.
  * `@hourly`: Runs every hour.
  * Cron expressions (e.g., `0 12 * * *` for noon daily).
* The **start_date** parameter determines when the DAG begins execution.

---

#### **Dependencies**

* Dependencies define the order in which tasks are executed.
* Methods to set dependencies:

  * **Bitshift Operators** : Use `>>` for downstream and `<<` for upstream dependencies.

  ```python
  task1 >> task2  # task1 runs before task2
  ```

  * **Explicit Methods** : Use `set_upstream()` or `set_downstream()` functions.

  ```python
  task2.set_upstream(task1)
  ```

---

# Tasks & Operators

In Apache Airflow, **Tasks** are the building blocks of workflows, and they represent individual units of work to be executed. Tasks are encapsulated within  **Operators** , which are predefined templates or logic for performing specific types of operations. Each operator defines what a Task will do.

Let me walk you through the commonly used Operators you mentioned:

### **PythonOperator**

* The **PythonOperator** allows you to execute Python functions as part of your workflow.
* You provide a callable (a function or method) that the operator will call when the Task runs.
* Example:

```python
from airflow.operators.python_operator import PythonOperator

def my_function():
    print("Hello, Airflow!")

python_task = PythonOperator(
    task_id='python_task',
    python_callable=my_function,
    dag=my_dag #Not needed if using "with DAG"
)
```

### **BashOperator**

* The **BashOperator** is used to execute bash commands or shell scripts.
* It's useful for running command-line utilities or scripts directly from Airflow.
* Example:

```python
from airflow.operators.bash_operator import BashOperator

bash_task = BashOperator(
    task_id='bash_task',
    bash_command='echo "Hello, Bash!"',
    dag=my_dag #Not needed if using "with DAG"
)
```

### **EmailOperator**

* The **EmailOperator** is used to send email notifications. You can configure recipients, subject, and body.
* It's useful for alerting or sharing information during the workflow execution.
* Example:

```python
from airflow.operators.email_operator import EmailOperator

email_task = EmailOperator(
    task_id='email_task',
    to='recipient@example.com',
    subject='Airflow Email Test',
    html_content='Hello, this is a test email from Airflow.',
    dag=my_dag #Not needed if using "with DAG"
)
```

### Key Points about Operators:

* Operators are abstract; they define what a Task does but not when or how it runs. Task dependencies and execution timing are defined separately in the DAG.
* There are other types of operators for different purposes, like SQL operators for database operations, HTTP operators for API calls, and so on.

# Task LifeCycle

In Apache Airflow, tasks go through various **lifecycle states** during their execution. These states help track the progress and outcome of tasks in your workflow. Here's an explanation of the key task states:

### **1. Success**

* A task enters the **Success** state when it has executed successfully without any errors or exceptions.
* This indicates that the operation defined by the task is complete and met the expected results.

### **2. Failed**

* A task is marked as **Failed** if it encounters an exception or error during its execution and cannot complete.
* Causes can include issues like invalid inputs, connection problems, or bugs in the task logic.

### **3. Skipped**

* Tasks are marked as **Skipped** when they are bypassed during workflow execution, typically due to a dependency condition not being met.
* This often occurs with conditional logic (e.g., using `ShortCircuitOperator`) or when upstream tasks set downstream tasks to be skipped.

### **4. Queued**

* A task is in the **Queued** state when it is waiting to be picked up by a worker for execution.
* It remains in the queue until a worker is available to execute it.

### **5. Running**

* A task is in the **Running** state when a worker is actively executing it.

### **6. Upstream Failed**

* A task enters the **Upstream Failed** state when one or more of its upstream (dependent) tasks fail, preventing it from running.
* This ensures that downstream tasks are not executed when their prerequisites are not satisfied.

### **7. Up for Retry**

* When a task fails but is configured with a  **retry policy** , it moves to the **Up for Retry** state.
* It waits for the specified retry delay before attempting to re-execute.

### **8. Deferred**

* In Airflow 2.2+ with Deferrable Operators, a task can enter a **Deferred** state to wait for an external event or condition without holding up a worker slot.

### **9. Removed**

* A task can be in the **Removed** state if it was removed from a DAG after previously being part of it. This occurs when an updated DAG no longer contains that task.

### **10. Shut Down**

* A task is marked as **Shut Down** when it is terminated due to a manual intervention or unexpected worker shutdown.

### Visualizing Task States

In the Airflow UI, you can monitor these states in the **Graph View** or  **Tree View** , where tasks are color-coded for easy identification. This helps in debugging and managing workflows effectively.

# Variables, Connections & XComs

In Apache Airflow, sharing data and configuration between tasks is critical for building dynamic workflows. Airflow provides several features to enable this:  **Variables** ,  **Connections** , and  **XComs** . Here’s how they work:

---

### **1. Variables**

* **What They Are** : Variables are key-value pairs that store global configuration values. These values can be accessed by any DAG or task in your Airflow environment.
* **Use Case** : Store configurations like file paths, credentials, or other constants that might change between environments (e.g., dev, staging, production).
* **Example** :

```python
from airflow.models import Variable

# Setting a variable (can also be done in the Airflow UI)
Variable.set("my_key", "my_value")

# Retrieving a variable
value = Variable.get("my_key")
print(value)  # Output: my_value
```

* **Where to Manage** : Variables can be managed via the  **Airflow UI** , the  **CLI** , or directly in Python scripts.

---

### **2. Connections**

* **What They Are** : Connections are configurations that allow Airflow to connect to external systems like databases, APIs, or cloud storage.
* **Use Case** : They abstract credentials and connection details, making it easy to set up and reuse in different tasks or operators.
* **Example** :
* Create a connection for a MySQL database in the Airflow UI or CLI.
* Use this connection in a task (e.g., with `MySqlOperator`):
  ```python
  from airflow.operators.mysql_operator import MySqlOperator

  mysql_task = MySqlOperator(
      task_id='mysql_query',
      sql='SELECT * FROM my_table',
      mysql_conn_id='my_mysql_connection',
      dag=my_dag
  )
  ```
* **Where to Manage** : Connections are managed via the **Airflow UI** under **Admin > Connections** or via the CLI.

---

### **3. XComs (Cross-Communications)**

* **What They Are** : XComs are used to pass small pieces of data between tasks. Each task can push and pull XComs.
* **Use Case** : Share dynamic values or intermediate results between tasks in the same DAG.

**Push Data**

```python
from airflow.operators.python_operator import PythonOperator

def push_xcom(**kwargs):
    ti = kwargs['ti'] # kwargs --> Key Word Arguments
    ti.xcom_push(key='my_key', value='Hello, XCom!')

push_task = PythonOperator(
    task_id='push_task',
    python_callable=push_xcom,
    provide_context=True,
    dag=my_dag
)
```

**Pull Data**

```python
def pull_xcom(**kwargs):
    value = kwargs['ti'].xcom_pull(task_ids='push_task', key='my_key')
    print(value)  # Output: Hello, XCom!

pull_task = PythonOperator(
    task_id='pull_task',
    python_callable=pull_xcom,
    provide_context=True,
    dag=my_dag
)
```

**Considerations** : XComs are stored in Airflow's metadata database and should only be used for small pieces of data, not large files.

---

By combining these features:

* **Variables** : Centralize and manage configuration values.
* **Connections** : Simplify access to external systems.
* **XComs** : Enable dynamic communication between tasks within a DAG.

.
