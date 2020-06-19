import numpy as np
import pandas as pd
from numpy.random import randn
from pandas import Series, DataFrame
import  matplotlib.pyplot as plt

arr1 = np.array([[10,np.nan,20], [30,40,np.nan]])
print(arr1)
df1 = DataFrame(arr1, index=[1,2], columns=list('ABC'))
print(df1)

#sum
print(df1.sum()) #sums along each column
print(df1.sum(axis=1)) #sum along indexes

print(df1.min()) #get minimum along each column
print(df1.max())

print(df1.idxmax())
print(df1.cumsum())
print(df1.describe())

df2 = DataFrame(randn(9).reshape(3,3), index=[1,2,3], columns=list('ABC'))
print(df2)
#plot the dataframe
plt.plot(df2)
plt.legend(df2.columns, loc='lower right')
plt.savefig('samplepic.png')
plt.show()
