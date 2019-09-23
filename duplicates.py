import importation as im

df = im.DataFrame(dict(col1=['uber', 'uber', 'uber', 'uber', 'grab'], col2=[5, 2, 4, 5, 6]))

print(df)

print(df.duplicated())

print(df.drop_duplicates())
print(df.drop_duplicates(['col1']))

print(df.drop_duplicates(['col1'], keep='last'))
