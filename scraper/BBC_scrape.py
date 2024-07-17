import requests
from bs4 import BeautifulSoup
import json

# Define the URL 
url = "https://www.bbc.com/news"
#Get Request
response = requests.get(url)
#check status
if response.status_code == 200:
    # Parsing
    soup = BeautifulSoup(response.content, 'html.parser')
    
    #fiinding all the major headlines using class
    headlines = soup.find_all('h2', class_='sc-4fedabc7-3 zTZri')
    
    # Extracting the text from the headlines
    headline_texts = [headline.get_text() for headline in headlines]
    
    # dataset
    data = {
        "headlines": headline_texts
    }
    
    # Define the file path where the JSON data will be stored
    json_file_path = 'headlines1.json'
    
    # Write the data to a JSON file
    with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    
    print(f"Data has been successfully scraped and stored in {json_file_path}")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
