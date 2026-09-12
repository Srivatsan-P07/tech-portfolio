import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import logging
logging.basicConfig(level=logging.ERROR)

import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.transforms.window import TimestampedValue

def parse_csv(line):
    sensor_id,temperature,event_time = tuple(line.split(','))
    return (sensor_id,float(temperature),int(event_time))

with beam.Pipeline(options=PipelineOptions()) as p:
    results = (
        p
        | "read" >> beam.io.ReadFromText('timestamp.csv',skip_header_lines=1)
        | "parse" >> beam.Map(parse_csv)
        | "timestamp" >> beam.Map(
            lambda x: TimestampedValue(
                (x[0], x[1]), x[2]
            )
        )
        | beam.Map(print)
    )