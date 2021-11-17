import os
import pandas as pd
from excel import Excel

# Create a Pandas dataframe from the data.
df = pd.DataFrame({
    'Name': ["Nhan", "Thong", "Duc Nhan"],
    'Age': [101, 201, 301],
})

# Create a Pandas Excel writer using XlsxWriter as the engine.
path = f"{os.getcwd()}/Day5/nhan/pandas_simple.xlsx"

excel = Excel(path)
excel.draw_table(df, "sheet 1")
excel.draw_table(df, "sheet 2")
excel.save()


