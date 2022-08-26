from extractcsv import read_csvfile_into_dataframe
from transform_3nf import third_normal_form
from writecsv import upload_blob

def GCSDataRead(event, context):
    bucketName = event['bucket']
    blobName = event['name']
    fileName = "gs://" + bucketName + "/" + blobName
    
    # extract
    df = read_csvfile_into_dataframe(fileName)

    # transform
    table_dict = third_normal_form(df) 

    # load
    csv_products = table_dict['products'].to_csv()
    csv_transactions = table_dict['transactions'].to_csv()
    csv_basket_items = table_dict['basket_items'].to_csv()

    upload_blob('bfairnington_appsbroker_task_transformed_data', csv_products, 'products.csv')
    upload_blob('bfairnington_appsbroker_task_transformed_data', csv_transactions, 'transactions.csv')
    upload_blob('bfairnington_appsbroker_task_transformed_data', csv_basket_items, 'basket_items.csv')









    

     




