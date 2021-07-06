import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data)

print(df)
print(df.loc[0])
print('___________________________________')
print('___________________________________')
print('___________________________________')
print('___________________________________')
print('___________________________________')
print('___________________________________')

# Pandas Read CSV

df = pd.read_csv('data.csv')

print(df.to_string())