**1. Pipeline & PCollection**

* **Concept:** `Pipeline` manages the execution graph (DAG). `PCollection` is the immutable, distributed dataset moving through the graph.

```python
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

options = PipelineOptions(runner='DataflowRunner', project='my-gcp-proj', temp_location='gs://my-bucket/temp')

with beam.Pipeline(options=options) as p:
    # 'lines' is an immutable PCollection
    lines = p | "Read" >> beam.io.ReadFromText("gs://my-bucket/input.txt")

```

---

**2. PTransform & ParDo / DoFn**

* **Concept:** `PTransform` is the processing step. `ParDo` applies user-defined logic element-by-element using a `DoFn`.

```python
class CleanTextFn(beam.DoFn):
    def process(self, element):
        # element: each item in the PCollection
        yield element.strip().lower()

# Usage in pipeline
cleaned = lines | "Clean" >> beam.ParDo(CleanTextFn())

```

---

**3. GroupByKey (GBK)**

* **Concept:** Shuffles and groups key-value pairs `(K, V)` into `(K, Iterable[V])`.
* *Interview note:* High memory risk on skewed keys; prefer `Combine` when possible.

```python
# Input: [('user_1', 10), ('user_1', 20), ('user_2', 5)]
grouped = (
    pairs 
    | "Group" >> beam.GroupByKey()
)
# Output: [('user_1', [10, 20]), ('user_2', [5])]

```

---

**4. CoGroupByKey**

* **Concept:** Performs a full outer join across multiple `(K, V)` PCollections on the same key type.

```python
# emails: [('user_1', 'a@x.com')], orders: [('user_1', 'item_101')]
joined = (
    {'email': emails, 'order': orders}
    | "JoinData" >> beam.CoGroupByKey()
)
# Output: [('user_1', {'email': ['a@x.com'], 'order': ['item_101']})]

```

---

**5. Combine (CombineFn)**

* **Concept:** Aggregates data associatively and commutatively (like a MapReduce Combiner), reducing network shuffle compared to `GroupByKey`.

```python
import apache_beam as beam

# CombineGlobally or CombinePerKey
totals_per_key = (
    pairs # ('user_1', 10), ('user_1', 20)
    | "SumPerKey" >> beam.CombinePerKey(sum)
)
# Output: ('user_1', 30)

```

---

**6. Side Inputs**

* **Concept:** Injects auxiliary/broadcast data (like a global lookup dictionary) into a `ParDo`.

```python
class EnrichFn(beam.DoFn):
    def process(self, element, lookup_map):
        user_id, amount = element
        country = lookup_map.get(user_id, 'UNKNOWN')
        yield (user_id, amount, country)

# lookup_pcoll passed as a side input using beam.pvalue.AsDict
enriched = main_pcoll | "Enrich" >> beam.ParDo(EnrichFn(), lookup_map=beam.pvalue.AsDict(lookup_pcoll))

```

---

**7. Additional (Side) Outputs / Tagged Outputs**

* **Concept:** Splits a single stream into multiple destination `PCollections` (e.g., valid records vs. dead-letter queue).

```python
class SplitFn(beam.DoFn):
    OUTPUT_VALID = 'valid'
    OUTPUT_DEADLETTER = 'dead_letter'

    def process(self, element):
        try:
            yield int(element) # Main output
        except ValueError:
            yield beam.pvalue.TaggedOutput(self.OUTPUT_DEADLETTER, element)

results = raw_records | "RouteData" >> beam.ParDo(SplitFn()).with_outputs(
    SplitFn.OUTPUT_DEADLETTER, 
    main=SplitFn.OUTPUT_VALID
)

valid_data = results[SplitFn.OUTPUT_VALID]
errors = results[SplitFn.OUTPUT_DEADLETTER]

```