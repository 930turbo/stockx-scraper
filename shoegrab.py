import requests
from bs4 import BeautifulSoup

def get_stockx_data(shoe_name):
    # Construct the URL for the StockX search page
    search_url = f"https://stockx.com/search/sneakers?q={shoe_name.replace(' ', '+')}"

    # Send an HTTP GET request to the StockX search page
    response = requests.get(search_url)
    response.raise_for_status()

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the first product listing
    product_link = soup.find('a', class_='tile browse-tile')

    if product_link:
        # Extract the product URL
        product_url = 'https://stockx.com' + product_link['href']

        # Send an HTTP GET request to the product page
        product_response = requests.get(product_url)
        product_response.raise_for_status()

        # Parse the HTML content of the product page
        product_soup = BeautifulSoup(product_response.text, 'html.parser')

        # Extract the required information
        last_sale = product_soup.find('div', class_='sale-value').text.strip()
        highest_sale = product_soup.find('div', class_='stats').find('div', class_='stats-high').text.strip()
        lowest_sale = product_soup.find('div', class_='stats').find('div', class_='stats-low').text.strip()
        volatility = product_soup.find('div', class_='stats').find('div', class_='stats-12').text.strip()
        num_sales = product_soup.find('div', class_='market-summary').find('div', class_='total-sales').text.strip()
        price_premium = product_soup.find('div', class_='market-summary').find('div', class_='average-price').text.strip()

        # Display the extracted information
        print(f"Last Sale: {last_sale}")
        print(f"Highest Sale: {highest_sale}")
        print(f"Lowest Sale: {lowest_sale}")
        print(f"Volatility: {volatility}")
        print(f"Number of Sales on StockX: {num_sales}")
        print(f"Price Premium: {price_premium}")
    else:
        print("No results found for the specified shoe.")

# Prompt the user for the shoe name
shoe_name = input("Enter a shoe name: ")

# Get data from StockX
get_stockx_data(shoe_name)
