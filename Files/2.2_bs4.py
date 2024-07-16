#Practice

import requests
from bs4 import BeautifulSoup

def main():

    url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
    r = requests.get(url)

    # Check status code for response received
    if r.status_code == 200:
        print("Successfully fetched the webpage!")

        soup = BeautifulSoup(r.content, 'html.parser') # Parsing the HTML content

        title = soup.title.string  # Extracting title of the page
        print(f"Title of the page: {title}")

        first_paragraph = soup.find('p').get_text()   # Extracting 1st paragraph
        print(f"First paragraph: {first_paragraph}")

        links = [a['href'] for a in soup.find_all('a', href=True)] # Extracting all links on the page\
            
        print(f"Number of links on the page: {len(links)}")
        for link in links:
                print(link)
    else:
        print(f"Failed to fetch the webpage. Status code: {r.status_code}")
        
if __name__ == "__main__":
    main()
    
'''
#Using BeautifulSoup:
-Pros:
1.Simplifies HTML parsing with intuitive methods (find, find_all).
2.Provides an API for navigating and extracting data from HTML/XML documents.
3.Handles complex HTML structures and errors.

-Cons:
1.Requires installing beautifulsoup4, adding an external dependency.
2.Adds a slight overhead compared to manual string parsing.

#Not Using BeautifulSoup in basic.py:
-Pros:
1.No external dependency, relying solely on built-in Python methods (find, split, etc.).
2.Offers full control over parsing logic and process.

-Cons:
1.Requires writing more verbose and error-prone code for HTML parsing.
2.Complex to handle nested or irregular HTML structures effectively without a dedicated parsing API.
'''