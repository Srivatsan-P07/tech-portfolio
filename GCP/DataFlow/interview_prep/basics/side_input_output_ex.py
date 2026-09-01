import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import logging
logging.basicConfig(level=logging.ERROR)

import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

class HighOrders(beam.DoFn):
    def process(self, line, threshold):
        if line.get('amount') >= threshold:
         yield line

"""
If each input row produces exactly one output row: use return + map
If one input may produce multiple outputs: use yield + flatmap

If using ParDo --> Use yield+flatmap
    # In a DoFn, process() is expected to return an iterable of output elements.
    # When Beam gets a dict from return line, it treats the dict itself as an iterable and iterates over its keys:
"""
def parse_csv(line):
    user, order, amount = tuple(line.split(','))
    return {"user": user, "amount": int(amount)}

with beam.Pipeline(options=PipelineOptions()) as p:
    threshold = p | beam.Create([200])
    output = (
        p
        | "read" >> beam.io.ReadFromText('orders.csv', skip_header_lines=1)
        | "parse" >> beam.Map(parse_csv)
        | "ParDo_Fn" >> beam.ParDo(
            HighOrders(),
            threshold=beam.pvalue.AsSingleton(threshold)
        )
        | "print" >> beam.FlatMap(print)
    )

class SplitOutputFn(beam.DoFn):
   def process(self, line):
      if line.get('amount') >= 200:
         yield line
      else:
         yield beam.pvalue.TaggedOutput('low', line)
      
with beam.Pipeline(options=PipelineOptions()) as p:
   output = (
      p
      | "read" >> beam.io.ReadFromText('orders.csv', skip_header_lines=1)
      | "parse" >> beam.Map(parse_csv)
      | "ParDo_fn" >> beam.ParDo(
         SplitOutputFn()
      ).with_outputs('low', main='high')
   )

   output.low | "low_print" >> beam.Map(print)
   output.high | "high_print" >> beam.Map(print)