import pandas as pd
import numpy as np
from pandas import  Series, DataFrame

#many to one merging
dframe1 = DataFrame({'reference':['ola', 'uber','lyft', 'gojek', 'grab'], 'revenue':[1, 2, 3, 4, 5]})
dframe2 = DataFrame({'reference':['ola', 'uber','lyft'], 'revenue':[1, 2, 3]})

# print(dframe1)
# print(dframe2)

df3 = pd.merge(dframe1, dframe2, on='reference')
# print(df3)

df4 = pd.merge(dframe1, dframe2, on='reference', how='left')
print(df4)

output = DataFrame(df4)
output.to_csv('outputcol.csv', sep=',')