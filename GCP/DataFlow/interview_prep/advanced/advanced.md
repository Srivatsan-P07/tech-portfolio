**Time Semantics**

* **Event Time vs. Processing Time:**
* *Event Time:* Timestamp generated at source (e.g., device log time).
* *Processing Time:* Clock time of the pipeline worker executing the step.
* *Example:*



```python
import apache_beam as beam
from apache_beam.transforms.window import TimestampedValue

# Attach event time from payload to element metadata
records = [("sensor_1", 25.4, 1714300000)]
pcoll = (
    pipeline
    | beam.Create(records)
    | "AddTimestamp"
    >> beam.Map(lambda x: TimestampedValue((x[0], x[1]), x[2]))
)

```

* **Watermark:**
* Beam's estimate of event-time completeness. When the watermark passes time $T$, the system assumes no more records with event time $\le T$ will arrive.



---

**Windowing Strategies**

```python
from apache_beam import window

# 1. Fixed (Tumbling): 60-second non-overlapping blocks
fixed_w = pcoll | beam.WindowInto(window.FixedWindows(60))

# 2. Sliding (Hopping): 60-second window moving every 10 seconds
sliding_w = pcoll | beam.WindowInto(window.SlidingWindows(size=60, period=10))

# 3. Session: Windows defined by a 30-minute inactivity gap per key
session_w = pcoll | beam.WindowInto(window.Sessions(gap_size=1800))

# 4. Global Window: Single infinite window across all data
global_w = pcoll | beam.WindowInto(window.GlobalWindows())

```

---

**Triggers, Allowed Lateness & Accumulation**

* **Triggers:** Control the exact moment window results are emitted.
* **Allowed Lateness:** Extra time window state stays alive to process late-arriving events.
* **Accumulation Modes:**
* `ACCUMULATING`: Subsequent firings include all prior window data plus new arrivals.
* `DISCARDING`: Each firing processes only data received since the previous firing.



```python
from apache_beam.transforms.trigger import (
    AfterCount,
    AfterWatermark,
    AccumulationMode,
)

windowed_stream = pcoll | beam.WindowInto(
    window.FixedWindows(60),
    # Trigger on watermark passing OR every 100 elements
    trigger=AfterWatermark(early=AfterCount(100)),
    # Accept late data up to 10 minutes past window end
    allowed_lateness=600,
    # Keep historical values in subsequent firings
    accumulation_mode=AccumulationMode.ACCUMULATING,
)

```