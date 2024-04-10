# Pandas: 
#    1) Series [Columns]
#    2) Data Frames [Combination of Multiple Series]

import pandas as pd

# print(pd.__version__)  # Way of Checking Pandas Version 

# ===================================================================

print('***************  Series ***************')

l1 = [11,22,33,44,55]

s1 = pd.Series(l1)

print("Series : \n",s1)

print("Type :",type(s1)) # Type of s1 : <class 'pandas.core.series.Series'>

# ===================================================================

print('***************  Data Frames ***************')

d1 = {'Tuple':('A','B','C','D','E'),'List':[11,22,33,44,55]} # In DataFrames We Can't use Set,dictionary bcz its unordered collections  

df1 = pd.DataFrame(d1,index=['line1','line2','line3','line4','line5']) # Index : u can give purticular name to your row
print('DataFrames :\n',df1)

# ===================================================================

print('***************  Reading Data from .csv ***************')
csv1 = pd.read_csv('data.csv')

csv1.index = [f'{i})' for i in range(1,len(csv1)+1)]
print(csv1)

# ===================================================================

print('***************  Pandas Inbuilt Fn ***************')

print(csv1.shape) # Returns Tuple (Rows,Columns)
print(csv1.head()) # head() return first n rows , Default value is 5
print(csv1.tail()) # tail() return last n rows , Default value is 5