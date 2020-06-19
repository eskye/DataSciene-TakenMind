import numpy as np
import pandas as pd
from numpy.random import randn
from pandas import Series, DataFrame

series1 = Series([100, 200, 300], index=['A','C','B'])
series2 = Series([300, 400, 500, 600], index=['A','B','C', 'D'])

#sorting by index
print(series1)
print(series1.sort_index())

#sort by value
print(series1.sort_values())

print(series1.rank())

#ranking of series

series3 = Series(randn(10))

print(series3)

print(series3.rank())
series3 = series3.sort_values()
print(series3.rank())