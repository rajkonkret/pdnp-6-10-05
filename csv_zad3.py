import pandas

# pip install pandas

data = pandas.read_csv('records2.csv', delimiter=";")
print(data)
#     name branch  year  cgpa
# 0  radek    coe     3   9.1
# 1  tomek    cot     2  19.1
# 2  zenek    cor     1   9.1
print(data.columns)
# Index(['name', 'branch', 'year', 'cgpa'], dtype='object')
print(data.values)
# [['radek' 'coe' 3 9.1]
#  ['tomek' 'cot' 2 19.1]
#  ['zenek' 'cor' 1 9.1]]
print(data.items)
# <bound method DataFrame.items of     name branch  year  cgpa
# 0  radek    coe     3   9.1
# 1  tomek    cot     2  19.1
# 2  zenek    cor     1   9.1>
