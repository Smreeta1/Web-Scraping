# Web Scraping

## Overview

This project demonstrates web scraping techniques using Python. 

## Directory Structure

- **`Files/`**: Contains basic web scraping details and examples using `bs4` and `MechanicalSoup`.
- **`scraper/`**: Includes the Python scripts for web scraping (`amazon_scrape.py`, `BBC_scrape.py`) and the scraped data files (`amazon_search_data.json`, `headlines1.json`).
- **`tests/`**: Contains test scripts (`test_amazon_scrape.py`) to validate the transformation process and generated data (`transformed1.json`) during testing.

## Setup

1. **Environment Setup**:
   - Ensure Python 3.x is installed.
   - Install dependencies using `pip install -r requirements.txt`.

2. **Running Tests**:
   - Navigate to the `tests/` directory.
   - Run tests with `pytest test_amazon_scrape.py`.

## Tests Overview

- **`test_amazon_scrape.py`**:
  - **`setup_transformed_data`**: Fixture to transform `amazon_search_data.json` and generate `transformed1.json`.
  - **`test_transform_rating_and_reviews_structure`**: Checks the structure of `transformed1.json`.
  - **`test_transform_rating_and_reviews_rating_format`**: Validates the rating format in `transformed1.json`.
  - **`test_compare_original_and_transformed`**: Compares `transformed1.json` with `transformed.json` to ensure consistency.


