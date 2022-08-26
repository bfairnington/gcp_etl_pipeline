import pandas as pd

def read_csvfile_into_dataframe(file_name: str):
    try:
        df = pd.read_csv(file_name)     
        return df
    except FileNotFoundError:
        return None