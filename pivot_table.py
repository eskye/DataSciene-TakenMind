import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
url = "https://en.wikipedia.org/wiki/Pivot_table"
dflist = pd.io.html.read_html(url)
df = dflist[0]
#new_header = df.iloc[0] # grab the first row for the header
#df = df[1:] #take the data less the header row
#df.columns = new_header #set the header row as the df header

# print(df)

print(df.pivot('Date of sale', 'Sales person', 'Total price'))