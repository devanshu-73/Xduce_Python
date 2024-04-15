# Beautiful soup : Scraping

from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.investing.com/earnings-calendar/'

response = requests.get(url)

page = BeautifulSoup(response.text,'html.parser')

row_data = []

all_data = page.find('table',{'id':'QBS_5_inner'})
for row in all_data.find_all('tr'):
    cells = row.find_all('td')
    row_cells = [cell.text.strip() for cell in cells if cell.text.strip()]
    if row_cells:
        row_data.append(row_cells)


print("===== List Data =====")
print(row_data)
print("===== DataFrame =====")
df = pd.DataFrame(row_data)
print(df)