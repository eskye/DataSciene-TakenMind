import numpy as np
import pandas as pd
from numpy.random import randn
from pandas import Series, DataFrame

series1 = Series([10, 20, 30 ,40], index=['a', 'b', 'c', 'd'])

print(series1)



#creating new indexes using reindex

series2 = series1.reindex(['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])

#using fillvalue
series2 = series2.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'i', 'j','k'], fill_value=10)
print(series2)

#using reindex methods => fill
cars = Series(['Audi', 'Merc', 'BMW'], index=[1, 2, 3])
print(cars)

rangers = range(13)
print(rangers)

cars = cars.reindex(rangers,method='ffill') #forward fill
print(cars)

#create new dataframe using randn
df1 = DataFrame(randn(25).reshape(5,5), index=['a', 'b', 'c', 'd', 'e'], columns=['c1', 'c2', 'c3', 'c4', 'c5'])
print(df1)

df2 = df1.reindex(['a','b', 'c', 'd', 'e','f'])
print(df2)

#reindex rows of Dataframe

#reindex of columns of Dataframe

df3 = df1.reindex(columns=['c1', 'c2', 'c3', 'c4', 'c5', 'c6'])
print(df3)

#using .ix[] to reindex

df4 = df1.loc[['a','b', 'c', 'd', 'e','f'], ['c1', 'c2', 'c3', 'c4', 'c5', 'c6']]
print(df4)