# Beam Classes

### **1. PCollections**

* A **PCollection** (Parallel Collection) is Apache Beam’s representation of a dataset.
* It is immutable, distributed, and can be processed in parallel.
* PCollections can hold data from various sources like a text file, a database, or a real-time data stream.
* They act as inputs and outputs for your transforms and can be either bounded (fixed size) for batch jobs or unbounded (grows over time) for streaming jobs.

For example:

```python
pcollection = pipeline | "Read Data" >> beam.io.ReadFromText('input.txt')
```

### **2. Pipelines**

* A **Pipeline** is the container for your entire data workflow. It represents the series of steps required to process your data.
* It is created using the `beam.Pipeline()` class and is responsible for managing the flow of data through the transforms.
* The steps in a pipeline can include reading, transforming, and writing data.

For instance:

```python
with beam.Pipeline() as pipeline:
    data = pipeline | "Read Data" >> beam.io.ReadFromText('input.txt')
```

### **3. Transforms**

* **Transforms** are operations applied to PCollections to modify, filter, or otherwise process the data.
* They are the building blocks of your pipeline, typically represented with the `>>` syntax (e.g., `PCollection | "Transform Name" >> beam.YourTransform`).
* Common transforms include:
  * **Map** : Apply a function to each element.
  * **Filter** : Keep only elements that meet a condition.
  * **GroupByKey** : Group elements by key for aggregation.

For example:

```python
transformed_data = pcollection | "Transform Data" >> beam.Map(lambda x: x.upper())
```

In summary:

* **PCollections** are your data.
* **Pipelines** are the overarching workflows.
* **Transforms** are the operations you perform on the data.
