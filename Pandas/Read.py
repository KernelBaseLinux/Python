import pandas as pd
def ReadCsvFile(a):
    df = pd.read_csv(a)
    print((df.to_string()))
