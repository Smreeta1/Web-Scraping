#Q.Write a program that grabs the full HTML from the page at the URL http://olympus.realpython.org/profiles.

import requests
from bs4 import BeautifulSoup
def main():

    url = 'http://olympus.realpython.org/profiles' #relative url
    r = requests.get(url)

    # Check status code for response received
    if r.status_code == 200:
        print("Successfully fetched the webpage!")

        soup = BeautifulSoup(r.content, 'html.parser')

        # Find all <a> tags and print their href attributes with the base URL
        base_url = 'http://olympus.realpython.org'  #base_url ,not relative url so define here again
        for link in soup.find_all("a"):
            full_url = base_url + link.get("href")
            print(full_url)

    
if __name__ == "__main__":
    main()
    