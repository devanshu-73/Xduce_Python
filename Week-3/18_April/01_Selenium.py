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

columns_data = [i.text for i in columns]
row_data = []

for row in rows:
    cells = row.find_elements(By.TAG_NAME,'td')
    data = [cell.text.strip() for cell in cells]
    if data:
        row_data.append(data)

# print("Columns:",columns_data)
# print("Rows:",row_data)



df = pd.DataFrame(row_data, columns=columns_data)
# print(df)

# Save the DataFrame to an Excel file
excel_file = "holiday_calendar.xlsx"
df.to_excel(excel_file, index=False)

print("Data saved to", excel_file)

driver.quit()
