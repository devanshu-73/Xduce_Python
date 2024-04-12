import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.investing.com/holiday-calendar/"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Find the table containing the holiday data
table = soup.find("table", {"id": "holidayCalendarData"})

# Extract data from the table
data = []
columns = []
for row in table.find_all("tr"):
    cells = row.find_all(["th", "td"])
    if len(cells) > 0:
        if not columns:
            columns = [cell.text.strip() for cell in cells]
        else:
            data.append([cell.text.strip() for cell in cells])

# Create a DataFrame from the extracted data
df = pd.DataFrame(data, columns=columns)

# Save the DataFrame to an Excel file
excel_file = "holiday_calendar.xlsx"
df.to_excel(excel_file, index=False)

print("Data saved to", excel_file)
