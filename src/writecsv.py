from google.cloud import storage

def upload_blob(bucket_name, data, destination_blob_name):

    # bucket
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)

    # file name
    blob = bucket.blob(destination_blob_name)

    # file
    blob.upload_from_string(data)
