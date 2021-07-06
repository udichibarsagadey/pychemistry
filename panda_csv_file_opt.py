'''from builtins import print

import pandas as pd



df = pd.read_csv('./data.csv')

print(df.head(10))
print(df.tail(10))

print(df.info())

print('_________________________________')

print('_________________________________')

import pandas as pd

df = pd.read_csv('data.csv')

df.dropna(inplace = True)

print(df.to_string())

'''

import pandas as pd

df = pd.read_csv('data.csv')

x = df["Calories"].mean()

df["Calories"].fillna(x, inplace = True)

print(df.to_string())

import pandas as pd

df = pd.read_csv('data.csv')

x = df["Calories"].mode()[0]

df["Calories"].fillna(x, inplace = True)
print(df.to_string())