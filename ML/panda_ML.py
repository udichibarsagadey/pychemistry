"""
how to write csv file in panda
1) Pandas head()
2) Pandas tail()
3) Pandas write csv ‘dtype’
4) Pandas write csv ‘true_values‘
5) Pandas write csv ‘false_values’

# pandas fillna
"""
import pandas as pd

ab = pd.read_csv('Fortune_10.csv')
print(ab)

print(ab.head())
print(ab.tail(7))

ab = pd.read_csv('student_results.csv')
print(ab)


# pandas interpolate()

ab = pd.interpolate()
print(ab)