import pandas as pd

filename = 'datasets.xlsx'

excelfile = pd.ExcelFile(filename)
sheetnames = excelfile.sheet_names
for sheetname in sheetnames:
    data_per_sheet = excelfile.parse(sheetname)
    data_per_sheet.to_csv(sheetname+'.csv', sep=',')

print('Done')
