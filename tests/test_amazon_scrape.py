import json
import os
import pytest
from scraper.amazon_scrape import transform_rating_and_reviews

def transform(input_file):
    # Call transform_rating_and_reviews with the adjusted input_file
    transformed_data = transform_rating_and_reviews(input_file)
    return transformed_data

@pytest.fixture
def setup_transformed_data():
    #directory path of this script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    #Path to the original amazon_search_data.json
    input_file = os.path.join(current_dir, '..', 'scraper', 'amazon_search_data.json')

    # transformed data
    transformed_data = transform(input_file)

    # Writing transformed data to a temporary JSON file in the tests directory
    transformed_file = os.path.join(current_dir, 'transformed1.json')
    with open(transformed_file, 'w') as f:
        json.dump(transformed_data, f, indent=4)

    yield transformed_file

    # Clean up after the test
    os.remove(transformed_file)

def test_transform_rating_and_reviews_structure(setup_transformed_data):
    with open(setup_transformed_data, 'r', encoding='utf-8') as f:
        transformed_data = json.load(f)
    assert isinstance(transformed_data, list)
    assert all(isinstance(item, dict) for item in transformed_data)
    for item in transformed_data:
        assert 'rank' in item
        assert 'title' in item
        assert 'author' in item
        assert 'weeks_on_list' in item
        assert 'rating' in item
        assert 'reviews' in item

def test_transform_rating_and_reviews_rating_format(setup_transformed_data):
    with open(setup_transformed_data, 'r', encoding='utf-8') as f:
        transformed_data = json.load(f)
    for item in transformed_data:
        rating_str = item['rating']
        if rating_str != 'N/A':
            rating_float = float(rating_str)
            assert 0 <= rating_float <= 5

def test_compare_original_and_transformed(setup_transformed_data):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Paths to the original and transformed files
    original_file = os.path.join(current_dir, '..', 'scraper', 'amazon_search_data.json')
    transformed_file_from_test = setup_transformed_data
    transformed_file_from_scraper = os.path.join(current_dir, '..', 'scraper', 'transformed.json')

    # Loading the transformed data from both files
    with open(transformed_file_from_test, 'r', encoding='utf-8') as f:
        transformed_data_from_test = json.load(f)
    
    with open(transformed_file_from_scraper, 'r', encoding='utf-8') as f:
        transformed_data_from_scraper = json.load(f)
    
    # Comparing the transformed data from both sources
    assert transformed_data_from_test == transformed_data_from_scraper


if __name__ == "__main__":
    pytest.main()
