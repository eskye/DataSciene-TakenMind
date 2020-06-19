import numpy as np
import pandas as pd
from numpy.random import randn
from pandas import Series, DataFrame

cars = Series(['A', 'B', 'C', 'D', np.nan])

# validate
print(cars.isnull())

# drop null values

# print(cars.dropna())

df = DataFrame([[1, 2, 3], [5, 6, np.nan, 10], [7, np.nan, 10], [np.nan, np.nan, np.nan]])
# print(df)

# print(df.dropna())
print(df.dropna(how='all'))

print(df.dropna(axis=1))  # column wise drop

df2 = DataFrame([[1, 2, 3, np.nan], [4, 5, 6, 7], [8, 9, np.nan, np.nan], [12, np.nan, np.nan, np.nan]])
print(df2)

print(df2.dropna(thresh=3))
print(df2.dropna(thresh=2))

#fillna
print(df2.fillna(0))
print(df2.fillna({0:0,1:50,2:100,3:200}))