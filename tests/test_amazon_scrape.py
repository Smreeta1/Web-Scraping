import os
import json
import pytest
from scraper.amazon_scrape import transform_rating_and_reviews

def test_transform_rating_and_reviews_structure():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    original_file = os.path.join(current_dir, '..', 'scraper', 'amazon_search_data.json')
    test_file = os.path.join(current_dir, 'tested_transformed.json')
    transformed_file_from_scraper = os.path.join(current_dir, '..', 'scraper', 'transformed.json')

    # Transform the data
    transformed_data = transform_rating_and_reviews(original_file)
    
    print("Data transformed")

    # Structure assertions
    assert isinstance(transformed_data, list), "Transformed data is not a list"
    assert all(isinstance(item, dict) for item in transformed_data), "Not all items in transformed data are dictionaries"
    for item in transformed_data:
        assert 'rank' in item, "Rank key is missing"
        assert 'title' in item, "Title key is missing"
        assert 'author' in item, "Author key is missing"
        assert 'weeks_on_list' in item, "Weeks_on_list key is missing"
        assert 'rating' in item, "Rating key is missing"
        assert 'reviews' in item, "Reviews key is missing"
    
    print("All assertions passed")

    # Save the asserted data to tested_transformed.json
    with open(test_file, 'w', encoding='utf-8') as f:
        json.dump(transformed_data, f, indent=4)
    
    print("Tested data saved to", test_file)

    # Load the transformed data from the preexisting transformed.json
    with open(transformed_file_from_scraper, 'r', encoding='utf-8') as f:
        transformed_data_from_scraper = json.load(f)

    # Compare the asserted data with transformed.json
    assert transformed_data == transformed_data_from_scraper, "Data mismatch between transformed and tested files"
    
    print("Data comparison passed")

    # Clean up after test
    if os.path.exists(test_file):
        os.remove(test_file)
        print("Test file removed after test")


def test_transform_rating_and_reviews_rating_format():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    original_file = os.path.join(current_dir, '..', 'scraper', 'amazon_search_data.json')
    test_file = os.path.join(current_dir, 'tested_transformed.json')

    # Transform the data
    transformed_data = transform_rating_and_reviews(original_file)
    
    print("Data transformed for rating format test")

    # Rating format assertions
    for item in transformed_data:
        rating_str = item['rating']
        if rating_str != 'N/A':
            rating_float = float(rating_str)
            assert 0 <= rating_float <= 5, "Rating out of expected range"
    
    print("Rating format assertions passed")

    # Save the asserted data to tested_transformed.json
    with open(test_file, 'w', encoding='utf-8') as f:
        json.dump(transformed_data, f, indent=4)
    
    print("Rating format tested data saved to", test_file)

    # Clean up after test
    if os.path.exists(test_file):
        os.remove(test_file)
        print("Test file removed after rating format test")

if __name__ == "__main__":
    pytest.main()