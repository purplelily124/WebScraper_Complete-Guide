import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "URL"
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

# Initialize lists to store data ; if there are two sections in the table
sectionA = []
sectionB = []

# Find all table rows
rows = soup.find_all("tr")

# Iterate through the rows
for row in rows:
    # Find all cells in the row
    cells = row.find_all("td")
    if cells:  # Check if the row has cells
        # Extract the text from the cells and append to the appropriate list
        if row.find_previous("th") and "sectionA" in row.find_previous("th").text:
            sectionA.append([cell.get_text(strip=True) for cell in cells])
        elif row.find_previous("th") and "sectionB " in row.find_previous("th").text:
            sectionB.append([cell.get_text(strip=True) for cell in cells])


# Create DataFrames
sectionA_df = pd.DataFrame(sectionA, columns=["Name", "Role"])
sectionB_df = pd.DataFrame(sectionB, columns=["Name", "Role"])

# Add headers to the DataFrames
sectionA_df["Department"] = "sectionA "
sectionB_df["Department"] = "sectionB "

# Concatenate the DataFrames
combined_df = pd.concat([sectionA_df, sectionB_df], ignore_index=True)

# Reorder columns to have "Department" as the first column
combined_df = combined_df[["Department", "Name", "Role"]]

# Export the combined DataFrame to a CSV file with headings
combined_df.to_csv("Newtable.csv", index=False, header=True)

print("Combined DataFrame saved to Newtable.csv")

print("sectionA")
print(sectionA_df)
print("\nsectionB")
print(sectionB_df)

