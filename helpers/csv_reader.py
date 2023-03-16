import pandas as pd

def read_csv(filename):
    df = pd.read_csv(filename)
    df.fillna("")
    return df