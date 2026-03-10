Overview

This project is a Python-based web scraper that extracts product information from a Target product listing page. It uses the Requests library to retrieve webpage content and BeautifulSoup to parse and extract product details such as product name, SKU, price, and availability.

The script sends a request to a Target webpage, analyzes the HTML structure, and collects relevant product data into a structured format.

Features

Scrapes product information from a Target webpage

Extracts key product details:

Product Name

SKU

Price

Availability

Handles missing fields using error handling

Returns structured product data in a Python list

Technologies Used

Python

Requests

BeautifulSoup (bs4)

Installation
1. Clone the Repository
git clone https://github.com/yourusername/target-product-scraper.git
cd target-product-scraper
2. Install Dependencies
pip install requests beautifulsoup4
Project Structure
target-product-scraper
│
├── scraper.py       # Main scraping script
├── README.md        # Project documentation
How It Works

The script sends an HTTP GET request to the Target webpage.

It checks if the request is successful.

BeautifulSoup parses the webpage HTML.

The script searches for product containers in the HTML.

Product information is extracted and stored in a list.

Usage

Run the script using Python:

python scraper.py

Example output:

{'Product Name': 'Wireless Headphones', 'SKU': '123456', 'Price': '$59.99', 'Availability': 'In Stock'}
{'Product Name': 'Bluetooth Speaker', 'SKU': '987654', 'Price': '$29.99', 'Availability': 'Out of Stock'}
Important Note

Target and many modern websites load product data dynamically using JavaScript. If the script does not return products, you may need to use tools like:

Selenium

Playwright

Target API endpoints

Future Improvements

Export data to CSV or JSON

Add logging

Implement Selenium for dynamic content

Schedule scraping jobs
