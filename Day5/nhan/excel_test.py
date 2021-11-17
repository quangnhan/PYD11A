import os
import pandas as pd

# Create a Pandas dataframe from the data.
df = pd.DataFrame({
    'Name': ["Nhan", "Thong", "Duc Nhan"],
    'Age': [101, 201, 301],
})

# Create a Pandas Excel writer using XlsxWriter as the engine.
path = f"{os.getcwd()}/Day5/nhan/pandas_simple.xlsx"
writer = pd.ExcelWriter(path, engine='xlsxwriter')

# Turn off the default header and skip one row to allow us to insert a
# user defined header.
df.to_excel(writer, sheet_name='Sheet1', startrow=1, header=False, index=False)

# Get the xlsxwriter workbook and worksheet objects.
workbook  = writer.book
worksheet = writer.sheets['Sheet1']

# Add a header format.
header_format = workbook.add_format({
    'bold': True,
    'text_wrap': True,
    'valign': 'top',
    'fg_color': '#D7E4BC',
    'border': 1})

# Write the column headers with the defined format.
for col_num, value in enumerate(df.columns.values):
    worksheet.write(0, col_num, value, header_format)

writer.save()