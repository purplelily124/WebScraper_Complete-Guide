import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "URL"
r = requests.get(url)

# Parse HTML content
soup = BeautifulSoup(r.content, "html.parser")

# Find the table
table = soup.find("table", class_="webGrid")

# Extract headers
headers = [th.text.strip() for th in table.find("thead").find_all("th")]

# Extract rows data
data = []
for row in table.find_all("tr")[1:]:
    row_data = [td.text.strip() for td in row.find_all("td")]
    data.append(row_data)

# Create DataFrame
df = pd.DataFrame(data, columns=headers)

# Save DataFrame to CSV
df.to_csv("table_data.csv", index=False)

print("DataFrame saved to CSV file successfully.")