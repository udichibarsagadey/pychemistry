import pandas as pd

df1 = pd.DataFrame({'ID':[1,2,3,4],
                    'class':[9,10,11,12]})
print(df1)
df2 = pd.DataFrame({'ID':[1,2,3,4],
                    'Name':['A','B','C','D']})
print(df2)
df3 = pd.DataFrame({'ID':[1,2,3,4],
                    'Age':[5,7,9,10]})
print(df3)
df4 = pd.DataFrame({'ID':[1,2,3,4],
                    'Marks':[90,40,50,80]})
print(df4)
b = pd.merge(df1,df2,df3,df4, on = 'ID')
print(b)