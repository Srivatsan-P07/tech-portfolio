import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import logging
logging.basicConfig(level=logging.ERROR)

import time

import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

class CleanTextFn(beam.DoFn):
    def process(self, element):
        yield element.strip().lower()

with beam.Pipeline(options=PipelineOptions()) as p:
    results = (
        p
        | "read" >> beam.io.ReadFromText('input.csv')
        | "pardo_func" >> beam.ParDo(CleanTextFn())
        | "mapit" >> beam.Map(print)
    )