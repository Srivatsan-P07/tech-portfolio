import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import logging
logging.basicConfig(level=logging.ERROR)

import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from datetime import datetime

def parsecsv(line):
    user_id,event_time,event_value = tuple(line.split(','))
    return (user_id,event_time,event_value)

with beam.Pipeline(options=PipelineOptions()) as p:
    result = (
        p
        | "read" >> beam.io.ReadFromText("timestamp2.csv", skip_header_lines=1)
        | "parsecsv" >> beam.Map(parsecsv)
        | beam.Map(print)
    )