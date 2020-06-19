import numpy as np
import pandas as pd
from numpy.random import randn
from pandas import Series, DataFrame

series1 = Series([100, 200, 300], index=['A','B','C'])
series2 = Series([300, 400, 500, 600], index=['A','B','C', 'D'])

#sum of series
print(series1 + series2)

#Dataframe

df1 = DataFrame(np.arange(4).reshape(2,2), columns=['a','b'], index=['car','bike'])
df2 = DataFrame(np.arange(9).reshape(3,3), columns=['a','b','c'], index=['car','bike','cycle'])
print(df1+df2)

df1 = df1.add(df2, fill_value=0)
print(df1)

series3 = df2.iloc[0]
print(df2 - series3)
