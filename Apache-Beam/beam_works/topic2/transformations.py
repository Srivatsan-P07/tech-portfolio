import apache_beam as beam
import sys

class Transformations:
    def __init__(self, transactions: str, pipeline_options: beam.options.pipeline_options.PipelineOptions):
        self.transactions = transactions
        self.pipeline_options = pipeline_options      

    def flatmapper(self, elements):
        flatmap_list = []
        transaction_id = elements[1]
        customer_id = elements[0]
        transaction_amount = elements[2]
        for item in elements[3].split('-'):
            return_tuple = customer_id, transaction_id, transaction_amount, item
            flatmap_list.append(return_tuple)
        
        return flatmap_list

    def partition_func(self, transformations, partitions):
        if transformations[1] >= 10000:
            return 0
        else:
            return 1

    def run(self):
        with beam.Pipeline(options=self.pipeline_options) as pipeline:
            headerless_data = (
                pipeline
                | "Read Data" >> beam.io.ReadFromText(self.transactions)
                | "Remove Header" >> beam.Filter(lambda row: not row.startswith('CustomerID'))
                | "Convert to List" >> beam.Map(lambda row: row.split(','))
                | "Get Items" >> beam.FlatMap(self.flatmapper)
            )

            customer_total = (
                headerless_data
                | "Customer K-V Tuple" >> beam.Map(lambda row: ( row[0], ( row[1], row[2], row[3] )))
                | "Group Customers" >> beam.GroupByKey()
                | "Customer Total" >> beam.Map( lambda kv: ( kv[0], sum( int(item[1]) for item in kv[1] ) ) )
            )

            spender_category = customer_total | "Partitioning" >> beam.Partition(self.partition_func, 2)
            spender_category[0] | 'HighNetWorth' >> beam.io.WriteToText('temp/HighPaying_Customers')
            spender_category[1] | 'LowNetWorth' >> beam.io.WriteToText('temp/LowPaying_Customers')

            item_count = (
                headerless_data
                | "Filter Refunds" >> beam.Filter(lambda row: int(row[2]) > 0)
                | "Item K-V Tuple" >> beam.Map(lambda row: ( row[3], ( row[0], row[1], row[2] )))
                | "Count Items" >> beam.combiners.Count.PerKey()
                | "Write Items" >> beam.io.WriteToText('temp/item_count')
            )

if __name__ == '__main__':
    pipeline_options = beam.options.pipeline_options.PipelineOptions(sys.argv)
    transformations = Transformations('transactions.csv', pipeline_options)
    transformations.run()
