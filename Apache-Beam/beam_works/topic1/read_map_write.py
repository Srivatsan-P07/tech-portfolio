import apache_beam as beam
import sys

class SimpleTransform():
    #map the init parameters
    def __init__(
        self, input_file: str, output: str, 
        pipeline_options: beam.options.pipeline_options.PipelineOptions
    ):
        self.input_file = input_file
        self.output_file = output
        self.pipeline_options = pipeline_options

    #get the pipeline with typecasting
    def read(self, pipeline: beam.Pipeline) -> beam.PCollection:
        #Since we got the pipeline directly from run , we dont have to create a new pipeline again
        pcollection = (
            pipeline
            | beam.io.ReadFromText(self.input_file)
        )
        return pcollection

    #get the read pcollection output as input
    def transform(self, input_pcollection: beam.PCollection) -> beam.PCollection:
        pcollection = (
            input_pcollection
            #transform to upper case
            | beam.Map(lambda row: row.upper())
        )
        return pcollection

    #get the transformed pcollection as input
    def write(self, transformed_pcollection: beam.PCollection):
        pcollection = (
            transformed_pcollection
            #write to file
            | beam.io.WriteToText(self.output_file)
        )
    
    #run the pipeline here, add self to call class parameters
    def run(self):
        #add any optional arguments inside the beam.pipeline() and then run the pipeline
        with beam.Pipeline(options=self.pipeline_options) as pipeline:
            input_pcollection = self.read(pipeline)
            transformed_pcollection = self.transform(input_pcollection)
            self.write(transformed_pcollection)

if __name__ == '__main__':
    #get the pipeline options from system arguments and pass it as a list
    pipeline_options = beam.options.pipeline_options.PipelineOptions(sys.argv)

    #Initialize SimpleTransform with init inputs
    st = SimpleTransform('temp/input.txt', 'temp/read_map_write_output.txt', pipeline_options)

    #Run the pipeline in the def run section
    st.run()
