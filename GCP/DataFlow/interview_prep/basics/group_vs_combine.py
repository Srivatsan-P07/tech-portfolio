import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import logging
logging.basicConfig(level=logging.ERROR)

import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

def parse_csv(line):
    user, order, amount = tuple(line.split(','))
    return (user, int(amount))

def parse_csv2(line):
    user_id,user_name,city = tuple(line.split(','))
    return (user_id, user_name)

with beam.Pipeline(options=PipelineOptions()) as p:
    results = (
        p
        | "read" >> beam.io.ReadFromText('orders.csv', skip_header_lines=1)
        | "parsecsv" >> beam.Map(parse_csv)
        | "groupbykey" >> beam.GroupByKey()
        | "print" >> beam.Map(print)
    )

with beam.Pipeline(options=PipelineOptions()) as p:
    orders = (
        p
        | "read1" >> beam.io.ReadFromText('orders.csv', skip_header_lines=1)
        | "parsecsv" >> beam.Map(parse_csv)
        | "combine" >> beam.CombinePerKey(sum)
        
    )
    users = (
            p
            | "read2" >> beam.io.ReadFromText('users.csv', skip_header_lines=1)
            | "parsecsv2" >> beam.Map(parse_csv2)
        )
    
    joined_data = (
        {'orders': orders, 'users': users}
        | beam.CoGroupByKey()
        | beam.Map(print)
    )