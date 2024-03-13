import requests
from bs4 import BeautifulSoup
import time
from docx import Document

# Function to scrape the website and extract text
def scrape_website(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the webpage
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract the text from the webpage
        text = soup.get_text()
        
        return text
    else:
        #Error message Block
        print("Error: Failed to retrieve the webpage")
        return None

# Function to save extracted text into a document file
def save_to_doc(text):
    doc = Document()
    doc.add_paragraph(text)
    doc.save("extractedtext.docx")

# Main function to run the scraping process
def main():
    # URL 
    college_url = "URL"
    
    # For the frequency of scraping (in seconds)
    scraping_interval = 3 * 30 * 24 * 60 * 60  # 3 months in seconds
    
    while True:
        # Scrape the website
        extractedtext = scrape_website(college_url)
        
        if extractedtext:
            # Save the extracted text to a document file
            save_to_doc(extractedtext)
            print("Website scraped successfully!")
        else:
            print("Failed to scrape website.")
        
        # Wait for the specified interval before scraping again
        time.sleep(scraping_interval)

# Run the main function
if __name__ == "__main__":
    main()