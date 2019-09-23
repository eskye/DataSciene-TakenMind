import numpy as np
import pandas as pd
from pandas import Series, DataFrame
file = '../demo.csv'
# dframe = pd.read_csv('../demo.csv')
dframe = pd.read_csv(file, header=None)
print(dframe)

#Use readTable
dframe2 = pd.read_table(file, sep=',', header=None)
print(dframe2)

#partial rows importing
print(pd.read_csv(file, nrows=2, header=None))

#dump
dframe2.to_csv('output.csv', sep='!')

#select specific columns
dframe.to_csv('dataouptu.csv', columns=[0, 1])
