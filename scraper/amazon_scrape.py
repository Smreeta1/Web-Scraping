import json
import requests
from bs4 import BeautifulSoup

def transform_rating_and_reviews(json_file):
    transformed_books = []
    
    with open(json_file, 'r') as f:
        books = json.load(f)
        
        for book in books:
            rating = book.get('rating', 'N/A')
            
            if " / " in rating:
                rating_parts = rating.split(" / ") 
                '''rating.split(" / "):
                Splits the rating string into a list rating_parts at the " / " delimiter
                '''
                rating_value = rating_parts[0].strip() #removes whitespace before and after
                
                # Extract reviews
                reviews_before = rating_parts[1].strip() #Retrieves the second part of rating_parts removing whitespace
                
                if "REVIEWS" in reviews_before:
                    reviews_before = reviews_before.replace("REVIEWS", "").replace(",", "").strip()
                    
                reviews_after = int(reviews_before) if reviews_before.isdigit() else "N/A"
            else:
                rating_value = "N/A"
                reviews_after = "N/A"
            
            transformed_book = {
                "rank": book['rank'],
                "title": book['title'],
                "author": book['author'],
                "weeks_on_list": book['weeks_on_list'],
                "rating": rating_value,
                "reviews": reviews_after
            }
            
            transformed_books.append(transformed_book)
    
    return transformed_books

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
    
    # Save scraped data to JSON file
    with open('amazon_search_data.json', 'w') as f:
        json.dump(books, f, indent=4)

    print(f"Scraped {len(books)} search results")
    print("Search data has been saved to amazon_search_data.json")


if __name__ == "__main__":
    scrape_amazon_charts()

    # Function call 
    transformed_data = transform_rating_and_reviews('amazon_search_data.json')

    # Print transformed data 
    print(json.dumps(transformed_data, indent=4))

    # Saving transformed data to JSON file
    with open('transformed.json', 'w') as f:
        json.dump(transformed_data, f, indent=4)

    print("Transformed data has been saved to transformed.json")
