import os
import pandas as pd

# Create a Pandas dataframe from the data.
df = pd.DataFrame({
    'Name': ["Nhan", "Thong", "Duc Nhan"],
    'Age': [101, 201, 301],
})

# # Create a Pandas Excel writer using XlsxWriter as the engine.
path = f"{os.getcwd()}/Day5/nhan/pandas_simple.xlsx"
writer = pd.ExcelWriter(path, engine='xlsxwriter')

# # Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Nathan')

# # Close the Pandas Excel writer and output the Excel file.
writer.save()