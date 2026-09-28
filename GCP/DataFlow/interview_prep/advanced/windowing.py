import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import logging
logging.basicConfig(level=logging.ERROR)

import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.transforms.window import TimestampedValue
from datetime import datetime
from apache_beam import window

def parsecsv(line):
    user_id,event_time,event_value = tuple(line.split(','))
    return (user_id,event_time,event_value)

with beam.Pipeline(options=PipelineOptions()) as p:
    result = (
        p
        | "read" >> beam.io.ReadFromText("timestamp2.csv", skip_header_lines=1)
        | "parsecsv" >> beam.Map(parsecsv)
        | beam.Map(
            lambda x: TimestampedValue(
                (x[0], int(x[2])), datetime.fromisoformat(x[1].replace('Z', '+00:00'))
            )
        )
        | beam.WindowInto(window.FixedWindows(60))
        | beam.CombinePerKey(sum)
        | beam.Map(print)
    )