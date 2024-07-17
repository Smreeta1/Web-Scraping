import json
import requests
from bs4 import BeautifulSoup

def scrape_amazon_charts():
    url = 'https://www.amazon.com/charts/mostsold/nonfiction' 
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    books = []
    
    # Loop through the book rankings
    for rank in range(1, 21):  #scraping the top 20 books
        rank_id = f"rank{rank}-mobile"
        book_section = soup.find("div", {"id": rank_id})
        
        if book_section:
            title_section = book_section.find("div", class_="kc-rank-card-title")
            author_section = book_section.find("div", class_="kc-rank-card-author")
            weeks_on_list_section = book_section.find("div", class_="kc-wol")
            rating_section = book_section.find("div", class_="numeric-star-data")
            
            title = title_section.text.strip() if title_section else "N/A"
            author = author_section.text.strip() if author_section else "N/A"
            weeks_on_list = weeks_on_list_section.text.strip() if weeks_on_list_section else "N/A"
            rating = rating_section.text.strip() if rating_section else "N/A"
            
            book_data = {
                "rank": rank,
                "title": title,
                "author": author,
                "weeks_on_list": weeks_on_list,
                "rating": rating
            }
            
            books.append(book_data)
    
    with open('amazon_search_data.json', 'w') as f:
        json.dump(books, f, indent=4)

    print(f"Scraped {len(books)} search results")
    print("Search data has been saved to amazon_search_data.json")

if __name__ == "__main__":
    scrape_amazon_charts()
