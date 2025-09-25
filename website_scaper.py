# *Note this is not a offical website scraper and can't be used for professional work this can only we used for small purposes or on example basis.*
import requests
from bs4 import BeautifulSoup

url = input("Enter URL here: ") # Here user will enter the url of the website. the url must be valid and start with (https://).

response = requests.get(url) # Here we GET requests has been made to the url.

soup = BeautifulSoup(response.text, 'html.parser') # Here we are using bs4 module to get the output beautifully
for body in soup.find_all("a"):
    print(body.text) # Here we are using for loop to get the any specific data from thw website