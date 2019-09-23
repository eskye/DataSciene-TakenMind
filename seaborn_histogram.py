import numpy as np
import pandas as pd
from numpy.random import randn
from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

ds1 = randn(1000)
ds2 = randn(100)

plt.hist(ds1)
plt.savefig('histImage.png')
# plt.show()


plt.hist(ds2)
plt.savefig('histImage2.png')
# plt.show()

plt.hist(ds1, density=True,color='green',bins=15,alpha=0.5)
plt.hist(ds2, density=True, bins=15,alpha=0.5)
plt.savefig('histImage3.png')
# plt.show()

#Seaborn Usage

ds3 = randn(1000)
ds4 = randn(1000)
sns_plot = sns.jointplot(ds3,ds4)
sns_plot.savefig('Imagesns.png')

sns_plot2 = sns.jointplot(ds3, ds4, kind='hex')
sns_plot2.savefig('heximage.png')

