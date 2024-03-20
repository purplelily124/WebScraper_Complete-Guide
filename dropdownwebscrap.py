from selenium import webdriver
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set the path to the ChromeDriver executable
chromedriver_path = "C:\softwares\chromedriver\chromedriver_win32\chromedriver.exe"
os.environ['PATH'] = f'{os.environ["PATH"]};{os.path.dirname(chromedriver_path)}'

# Initialize Chrome options
options = Options()
options.add_argument("--headless")  # Add any desired options here

# Initialize WebDriver without 'executable_path' argument
driver = webdriver.Chrome(options=options)

# Navigate to the website
driver.get("link")

# Wait for the button to be clickable
button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "accordion"))
)

# Click the button to expand the dropdown
button.click()

# Wait for the panel to be visible
panel = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "panel"))
)

# Extract text from the panel
text = panel.text
print(text)

# Close the browser
driver.quit()
