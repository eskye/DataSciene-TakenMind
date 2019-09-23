import pandas as pd
from pandas import DataFrame
import seaborn as sns
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

filename = 'datasetsFiveYearData'
df = sns.load_dataset('https://raw.githubusercontent.com/resbaz/r-novice-gapminder-files/master/data/gapminder-FiveYearData')
dtf = DataFrame(df)
dff = dtf.drop_duplicates(['year', 'continent'], keep='last')
df2 = dff.pivot('year', 'continent', 'lifeExp')

# Plot the graph
sns.heatmap(df2).get_figure().savefig('finaloutput.png')
