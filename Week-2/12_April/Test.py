import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.investing.com/holiday-calendar/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

response = requests.get(url, headers=headers)
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
            # Extract column headers
            columns = [cell.text.strip() for cell in cells]
        else:
            # Extract row data
            data.append([cell.text.strip() for cell in cells])

# Create a DataFrame from the extracted data
df = pd.DataFrame(data, columns=columns)

# Save the DataFrame to an Excel file
excel_file = "holiday_calendar.xlsx"
df.to_excel(excel_file, index=False)

print("Data saved to", excel_file)
