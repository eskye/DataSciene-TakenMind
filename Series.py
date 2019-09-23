import pandas as pd
from pandas import Series
import numpy as np
object = Series([5, 10, 15, 20])
# print(object)
# print(object.values)
# print(object.index)

#use numpy array to create series
data_arr = np.array(['a', 'b', 'c'])
s = Series(data_arr)
# print(s)

#Customize Series Index
s = Series(data_arr, index=[100, 101, 102])

s = Series(data_arr, index=['index1', 'index2', 'index3'])
# print(s)

#using real life ex
revenue = Series([20, 80, 40, 35], index=['ola','uber', 'grab', 'gojek'])
#print(revenue)

#using condition within series

#print(revenue[revenue >= 35])

#use boolean conditions
#print('ola' in revenue)

revenue_dict = revenue.to_dict()
# print(revenue_dict)

#nan values

index_2 = ['ola', 'uber', 'grab', 'gojek', 'lyft']
revenue2 = Series(revenue, index_2)
# print(revenue2)

null = pd.isnull(revenue2)
null = pd.notnull(revenue2)
print(null)

#addition of series (+)
added_rev = revenue + revenue2
print(added_rev)

#assigning names

revenue2.name = "Company Revenues"
revenue.index.name = "Company Name"
print(revenue2)
print(revenue)
