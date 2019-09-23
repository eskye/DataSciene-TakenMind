import pandas as pd
from pandas import Series, DataFrame
import numpy as np

#example of Revenue of Companies
revenue_pdf = pd.read_clipboard(sep=r"\\s%")
# print(revenue_pdf)
#index and colums
# print(revenue_pdf.columns)
# print(revenue_pdf['Rank'])

#multiple columns
s = DataFrame(revenue_pdf, columns=['Rank', 'Name', 'Industry'])
# print(s)

#Nan Values
revenue_pdf2 = DataFrame(revenue_pdf, columns=['Rank', 'Name', 'Industry', 'Profit'])
print(revenue_pdf2)

#hail and tail
#print(revenue_pdf.head(2)) #print the first two rows
#print(revenue_pdf.tail(2)) # Print the last two rows

#access rows in Dataframe
#print(revenue_pdf.loc[3])

# assign values to df
#numpy
array1 = np.array([1, 2, 3, 4, 5, 6])
# revenue_pdf2['Rank'] = array1
# print(revenue_pdf2)

#series
profits = Series([900, 1000], index=[3, 5])
# revenue_pdf2['Profit'] = profits
# print(revenue_pdf2)

#deletion
del revenue_pdf2['Profit']
print(revenue_pdf2)

#dictionary function to dataframe
sample = {
    'company':['A', 'B'],
    'Profit':[1000, 5000]
}
print(sample)

sample_df = DataFrame(sample)
print(sample_df)