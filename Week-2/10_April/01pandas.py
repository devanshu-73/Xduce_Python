# Pandas: 
#    0) Pandas Installation , Importing into Python file
#    1) Series [Columns]
#    2) Data Frames [Combination of Multiple Series]
#    3) Reading Data from Excel Sheet
#    3) Reading Data from CSV File [Comma Separate Values]
#    4) Pandas Inbuilt Fns : count(),head(),tail(),value_counts(),sum(),max(),min(),mean()
#    4) Pandas attributes : shape,columns

import pandas as pd

print(pd.__version__)  # Way of Checking Pandas Version 

# ===================================================================

print('***************  Series ***************')

l1 = [11,22,33,44,55]
s1 = pd.Series(l1)
print("Series :",s1)
print("Type :",type(s1)) # Type of s1 : <class 'pandas.core.series.Series'>

# ===================================================================

print('***************  Data Frames ***************')

d1 = {'Tuple':('A','B','C','D','E'),'List':[11,22,33,44,55]} # In DataFrames We Can't use Set,dictionary bcz its unordered collections  

df1 = pd.DataFrame(d1,index=['line1','line2','line3','line4','line5']) # Index : u can give purticular name to your row
print('DataFrames :\n',df1)

# ===================================================================

"""   
    If We Have File's Path like below then it gives error,
    so u have to write 'r' before your path so it consider as a raw string
    print(r'C:/Users/Devanshu Chauhan/Desktop/Devanshu-python/Week-2/10_April/data.csv')

    or u can do this

    print('C:\\Users\\Devanshu Chauhan\\Desktop\\Devanshu-python\\Week-2\\10_April\\data.csv')

"""

print('***************  Reading Data from Excel Sheet ***************')

excel1 = pd.read_excel('data.xlsx')
print(excel1)

print('***************  Reading Data from CSV[Comma Separate Values] ***************')

csv1 = pd.read_csv('data.csv')

csv1.index = [f'{i})' for i in range(1,len(csv1)+1)]        
print(csv1) # All Data
print(csv1['Name']) # Purticular Series(Column) Data
print(csv1[['Name','Age']]) # Purticular Series(Column) Data        
# ===================================================================

print('***************  Pandas Inbuilt Fn ***************')

# Functions
print(csv1.head()) # head() return first n rows , Default value is 5
print(csv1.tail()) # tail() return last n rows , Default value is 5 
print(csv1['Gender'].value_counts()) # Returning Specific counts like male=14,female=10
print(csv1['Name'].count()) # count() return how many entries have that column

# Attributes
print(csv1.shape) # Returns Tuple (Rows,Columns)
print(csv1.columns) # Returns All Columns