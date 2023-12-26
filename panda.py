# print("hello world")

# pandas allows you to work with big data, better than excel

# going to load it into a dataframe, that is the object type that pandas allows you to
# manipulate everything with

# .head(x) to see top x rows
# .tail()

# print(df.head(30))

# df_xls = pd.read_excel('pokemon_data.xlsx')

#('pokemon_data.txt', delimiter='\t')

import pandas as pd

df = pd.read_csv('pokemon_data.csv')

# .head(x) to see top x rows
# .tail()

# print(df.head(30))

## read headers
#print(df.columns)

## read each column
# df.Name doesn't really work for two word names
#print(df[['Name', 'Type 1', 'HP']][0:5])

## read each row
# integer location
#.iloc[0:4]
# print(df.iloc[1])
# iterate rows
# for index, row in df.iterrows():
#     print(index, row['Name'])
# print(df.loc[df['Type 1'] == "Fire"])

## read a specific location (R, C)
# print(df.iloc[2,1])

# mean, std dev stats
# print(df.describe())
# print(df.sort_values('Name', ascending=False))

# print(df.sort_values(['Type 1', 'HP'], ascending=[True, False]))

## changing data
# make sure to double-check it was done correctly

# adding col
# df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']

# deleting col
# df = df.drop(columns=['Total'])

# end param is exclusive
df['Total'] = df.iloc[:, 4:10].sum(axis=1)

print(df.head(5))