# Selenium 
# pip install selenium
# pip install webdriver-manager

import time
import pandas as pd 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://www.investing.com/holiday-calendar/')

table_element = driver.find_element(By.ID, 'holidayCalendarData')

columns = table_element.find_elements(By.XPATH, '//*[@id="holidayCalendarData"]/thead[1]/tr/th')
rows =  table_element.find_elements(By.TAG_NAME,'tr')

data = []
# columns_data = [i.text for i in columns]
# print("Columns:",columns_data)

for row in rows:
    cells = row.find_elements(By.TAG_NAME,'td')
    row_data = [cell for cell in cells if len(cell.text) != 0]
    data.append(row_data)

# print("Rows:",data)



# df = pd.DataFrame(data[2:], columns=data[0])
# print(df)

driver.quit()
