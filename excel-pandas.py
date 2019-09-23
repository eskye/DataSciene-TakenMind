import pandas as pd

#xlrd
#openpyxl
file = 'demo2.xlsx'
excelfile = pd.ExcelFile(file)
dframe = excelfile.parse('demo2')
print(dframe)
