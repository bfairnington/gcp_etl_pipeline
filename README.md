A functioning extract-transform-load (ETL) data pipeline created to work with Google Cloud Platform (GCP). The setup does not use infrastructure as code (IAC) so the setup would have to be carried out manually in GCP. This includes the following:

- Raw data Google Cloud Storage bucket (to hold the raw data .csv files)
- Transformed data Google Cloud Storage bucket (to hold the transformed data .csv files)
- An extract and transform Google Cloud Function (copy the .py python files from the "extract and transform" folder here)
- A load Google Cloud Function (copy the .py python files from the "load" folder here)
- A database in Google Big Query
- Queries can be run using SQL and optionally visualised using Google Data Studio as desired
