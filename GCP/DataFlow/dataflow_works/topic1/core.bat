python read_map_write.py ^
    --runner=DataflowRunner ^
    --project=srivatsan-paid-learning ^
    --temp_location=gs://hawx_dataflow_bucket/temp ^
    --staging_location=gs://hawx_dataflow_bucket/stg ^
    --job_name=read-map-write ^
    --worker-machine-type=n1-standard-1 ^
    --region=asia-south1 ^
    --service_account_email=dataflow-service-account@srivatsan-paid-learning.iam.gserviceaccount.com ^
    --requirements_file=requirements.txt