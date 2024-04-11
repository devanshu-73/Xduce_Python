# Pandas :
# 1) Getting Data Using Single Condition
# 2) Getting Data Using Multiple Condition : use &(and),|(or)
# 3) Adding Column
# 4) Function : apply(your_function_name)  
# 5) Save the modified DataFrame into New_File and Original File
# 6) Droping(Deleting) Row,columns : drop()


import pandas as pd
csv_data = pd.read_csv('data.csv')

# ===============================================================================

# Getting Data : Single Condition

print(csv_data[csv_data['Gender']== 'Male'])

# ===============================================================================

# Getting Data : Multiple Condition

print(csv_data[(csv_data['Gender']== 'Male') & (csv_data['Age'] >= 30)])

# ===============================================================================

# Adding Column

csv_data['Salary'] = csv_data['Age']*1000

# ===============================================================================

# Function : apply(your_function_name) : apply Function on series(Column)

def joining_bonus(x):
    if x <= 25000:
        return 3000
    else:
        return 'N/A'

csv_data['Joining Bonus'] =  csv_data['Salary'].apply(joining_bonus)

# ===============================================================================

# Save the modified DataFrame in to new file
csv_data.to_csv('data_with_salary.csv', index=False)

# Save the modified DataFrame in to new file
csv_data.to_csv('data.csv', index=False)

# ===============================================================================
 
# Droping(Deleting) Row : drop(index = row_number,inplace=True(original_file affected))
# Droping(Deleting) Columns : drop(columns='column_name',inplace=True(original_file affected))

#Row
print(csv_data.drop(index=0)) # First row deleted not permanently
print(csv_data.drop(index=0,inplace=True)) # First row deleted permanently

# Column

print(csv_data.drop(columns='Joining Bonus')) # Column deleted not permanently
print(csv_data.drop(columns='Joining Bonus',inplace=True)) # Column deleted permanently


# ===============================================================================
