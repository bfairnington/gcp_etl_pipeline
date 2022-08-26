from google.cloud import bigquery

def load():

     # Construct a BigQuery client object.
     client = bigquery.Client()

     # TODO(developer): Set table_id to the ID of the table to create.
     # table_id = "your-project.your_dataset.your_table_name"

     job_config = bigquery.LoadJobConfig(
     schema=[
          bigquery.SchemaField("name", "STRING"),
          bigquery.SchemaField("post_abbr", "STRING"),
     ],
     skip_leading_rows=1,
     # The source format defaults to CSV, so the line below is optional.
     source_format=bigquery.SourceFormat.CSV,
     )
     uri = "gs://cloud-samples-data/bigquery/us-states/us-states.csv"

     load_job = client.load_table_from_uri(
     uri, table_id, job_config=job_config
     )  # Make an API request.

     load_job.result()  # Waits for the job to complete.

     destination_table = client.get_table(table_id)  # Make an API request.
     print("Loaded {} rows.".format(destination_table.num_rows))

# Load data into BigQuery
def load_data_from_gcs(dataset, table1, source ):
    bigquery_client = bigquery.Client(dataset)
    dataset = bigquery_client.dataset('pageSpeed')
    table = dataset.table(table1)
    job_name = str(uuid.uuid4())

    job = bigquery_client.load_table_from_storage(
        job_name, table, "gs://psi-reports")

    job.source_format = 'NEWLINE_DELIMITED_JSON'
    job.begin()
    wait_for_job(job)
    print("state of job is: " + job.state)
    print("errors: " + job.errors)


