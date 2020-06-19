import numpy as np
import pandas as pd
from numpy.random import randn
from pandas import Series, DataFrame

series1 = Series([100, 200, 300], index=['A','B','C'])

print(series1['A'])
print(series1[['A','B']])

#number indexes
print(series1[0])
print(series1[0:2])

#conditional indexes

print(series1[series1 > 150])

#using df and accessing df

df1 = DataFrame(np.arange(9).reshape(3,3), index=['car','bike','cycle'],columns=['A','B','C'])
print(df1)
print(df1['A'])
print(df1[['A', 'B']])

print(df1 > 5)

#using ix function
print(df1.iloc[1]) #use index
print(df1.loc['bike']) #use key in string