# Beautiful soup : Scraping

from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt

url = 'https://www.investing.com/earnings-calendar/'

response = requests.get(url)

page = BeautifulSoup(response.text,'html.parser')

row_data = []
row = []
column = ['Current_Price','Change','Gain%']

all_data = page.find('table',{'id':'QBS_5_inner'})
for rowi in all_data.find_all('tr'):
    cells = rowi.find_all('td')
    row_cells = [cell.text.strip() for cell in cells if cell.text.strip()]
    row_data.append(row_cells[1:])

    for i in row_cells[0:1]:
        row.append(i)
print(row)
print("===== List Data =====")
print(row_data)
print("===== DataFrame =====")
df = pd.DataFrame(row_data,index = row,columns = column)
print(df)

csv_file = "stocks.csv"
df.to_csv(csv_file, index=False)

# # Plotting
# plt.figure(figsize=(12, 8))
# for stock in df.index:
#     plt.bar(df.columns, df.loc[stock], label=stock)

# plt.xlabel('Metric')
# plt.ylabel('Value')
# plt.title('Stock Data')
# plt.legend()
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()
