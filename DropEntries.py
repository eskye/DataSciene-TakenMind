import numpy as np
import pandas as pd
from numpy.random import randn
from pandas import Series, DataFrame

cars = Series(['Audi', 'Merc', 'BMW'], index=['a', 'b', 'c'])
print(cars)

cars = cars.drop('a')
print(cars)

#dataframes
carsdf = DataFrame(np.arange(9).reshape(3,3), index=['BMW', 'Audi','Merc'], columns=['rev','pro','exp'])
print(carsdf)

carsdf = carsdf.drop('BMW', axis=0)
print(carsdf)

carsdf = carsdf.drop('pro', axis=1)
print(carsdf)