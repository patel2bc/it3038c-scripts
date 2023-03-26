# Import required libraries 
import requests
from bs4 import BeautifulSoup

# Set the keh.com product URL
url = input('Enter a keh.com product URL:')

# GET request to pull in html data
response = requests.get(url)
html_content = response.content

# Setup HTML parser 
soup = BeautifulSoup(html_content, 'html.parser')

# Find and set name/price elements, for KEH, it was "page-title" and "price-wrapper"
name = soup.find('h1', {'class': 'page-title'})
price = soup.find('span', {'class': 'price-wrapper'})

# Check if the price was found
if price is not None:
    name = name.text.strip()
    price = price.text.strip()
    print(name)
    print(price)
else:
    print('Could not find price element')

# Script made by Bunci Patel
# Sources: https://www.digitalocean.com/community/tutorials/how-to-work-with-web-data-using-requests-and-beautiful-soup-with-python-3
#          https://stackoverflow.com/questions/39757805/using-python-requests-and-beautiful-soup-to-pull-text
#          https://www.zenrows.com/knowledge/python-requests-and-beautifulsoup-integration
#          https://www.keh.com/

