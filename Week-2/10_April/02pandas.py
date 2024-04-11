# Pandas :
# 1) Getting Data Using Single Condition
# 2) Getting Data Using Multiple Condition : use &(and),|(or)


import pandas as pd
csv_data = pd.read_csv('data.csv')

# Getting Data : Single Condition

print(csv_data[csv_data['Gender']== 'Male'])

# Getting Data : Multiple Condition

print(csv_data[(csv_data['Gender']== 'Male') & (csv_data['Age'] >= 30)])
