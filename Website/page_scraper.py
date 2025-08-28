# Website/Page scraper:
import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.google.com") # Here we are doing get request to receive html source code.

# Here we are using bs4 module so that data we are receiving will be printed in good looking manner.
soup = BeautifulSoup(response.text, 'html.parser')
for body_content in soup.find_all("body"):
    print(body_content.text)

# Here i used google.com you can use any website url but that url must be correct and valid.