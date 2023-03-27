import requests
from bs4 import BeautifulSoup
import re

website = input("Enter a website: ")
response = requests.get(website)
soup = BeautifulSoup(response.content, "html.parser")

# Finds common terms within website 
contact_terms = ["contact", "support", "help", "phone", "email"]
contact_info = []

for term in contact_terms:
    for element in soup.find_all(string=lambda text: text and term in text.lower()):
        if "@" in element:
            contact_info.append(element.strip())
        elif any(char.isdigit() for char in element):
            contact_info.append(element.strip())

# If no contact information found, it will try to find a contact us or about us page 
if not contact_info:
    contact_pages = ["contact", "about"]
    for page in contact_pages:
        contact_url = website + "/" + page
        response = requests.get(contact_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            for term in contact_terms:
                for element in soup.find_all(string=lambda text: text and term in text.lower()):
                    if "@" in element:
                        contact_info.append(element.strip())
                    elif any(char.isdigit() for char in element):
                        contact_info.append(element.strip())

# Output 
for info in contact_info:
    email_match = re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', info)
    phone_match = re.search(r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b', info)
    if email_match:
        print("Email: ", email_match.group())
    elif phone_match:
        print("Phone: ", phone_match.group())
