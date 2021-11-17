import pandas as pd

class Excel:
    def __init__(self, path):
        self.__writer = pd.ExcelWriter(path, engine='xlsxwriter')
    
    def draw_table(self, df, sheet_name):
        df.to_excel(self.__writer, sheet_name=sheet_name, startrow=1, header=False, index=False)
        
        # Get the xlsxwriter workbook and worksheet objects.
        workbook  = self.__writer.book
        worksheet = self.__writer.sheets[sheet_name]

        # Add a header format.
        header_format = workbook.add_format({
            'bold': True,
            'text_wrap': True,
            'valign': 'top',gi
            'fg_color': '#D7E4BC',
            'border': 1})

        # Write the column headers with the defined format.
        for col_num, value in enumerate(df.columns.values):
            worksheet.write(0, col_num, value, header_format)  
    
    def save(self):
        self.__writer.save()