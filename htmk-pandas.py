import pandas as pd
from pandas import DataFrame
from pandas import read_html
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
url = "https://countrycode.org/"
dflist = pd.io.html.read_html(url)
dframe = dflist[0]
# print(dflist)

print(dframe.columns.values)