import requests
from bs4 import BeautifulSoup

# Function to scrape product data
def scrape_target_products(url):
    # Send GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code != 200:
        print("Failed to retrieve the webpage.")
        return None
    
    # Parse the content using Beautiful Soup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find product containers
    products = soup.find_all('div', class_='product-container')  # Change this according to the website's structure

    product_list = []
    
    # Iterate through the product containers and extract details
    for product in products:
        try:
            name = product.find('h2', class_='product-name').get_text(strip=True)
            sku = product['data-sku']  # Example, modify based on actual attribute for SKU
            price = product.find('span', class_='product-price').get_text(strip=True)
            availability = product.find('span', class_='product-availability').get_text(strip=True)

            product_list.append({
                'Product Name': name,
                'SKU': sku,
                'Price': price,
                'Availability': availability
            })
        except AttributeError as e:
            print(f"Error extracting product details: {e}")

    return product_list

# URL of the Target product page (example)
url = 'https://www.target.com/c/products/-/N-5xtg0'  # Replace with the actual URL

# Execute the scraping function
products = scrape_target_products(url)

# Display the extracted product data
if products:
    for product in products:
        print(product)