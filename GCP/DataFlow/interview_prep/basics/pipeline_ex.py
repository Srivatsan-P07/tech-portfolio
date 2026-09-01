import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import logging
logging.basicConfig(level=logging.ERROR)

import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions


with beam.Pipeline(options=PipelineOptions()) as p:
    lines = (
        p 
        | "read" >> beam.io.ReadFromText('input.csv')
        | "show" >> beam.Map(print)
    )
    