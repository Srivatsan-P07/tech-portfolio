### **Spark Architecture**

1. **Spark Components**:
   - **Driver**: The driver program runs the main function of the application and creates the SparkContext. It is responsible for converting user code into tasks that can be executed by the executors.
   - **Executors**: Executors are distributed across the cluster and are responsible for running the tasks assigned by the driver. They also store data in memory or disk storage.
   - **Cluster Manager**: The cluster manager allocates resources across the cluster. Spark can work with various cluster managers like Hadoop YARN, Apache Mesos, Kubernetes, or its own standalone cluster manager.

2. **DAG (Directed Acyclic Graph)**:
   - Spark uses a DAG to represent a series of computations. When an action is called, Spark constructs a DAG of stages and tasks to be executed.
   - The DAG ensures that tasks are executed in the correct order and optimizes the execution plan for efficiency.

3. **Lazy Evaluation**:
   - Spark employs lazy evaluation, meaning it doesn't immediately execute transformations (like map, filter) on data. Instead, it builds up a plan of transformations.
   - Actual computation is triggered only when an action (like count, collect) is called. This approach helps optimize the execution plan and improve performance.