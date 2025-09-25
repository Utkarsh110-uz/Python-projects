# *Note this is not an professional news app code it can be used for temp purpose or project purpose.*
import requests
import json

search = input("Search for the news here: ") # Here user will enter the type of news he/she wants to see
response = requests.get(f"https://newsapi.org/v2/everything?q={search}&from=2025-07-29&sortBy=publishedAt&apiKey=58b04830080d43ad99c2c52672d4bef5") # Here we are sending get request and bring back some data and store is in response variable
news = json.loads(response.text) # Here we are doing some changes using json module and then storing it in news variable
for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print(article["url"])
    print("-----------------------------------------") # Here we are getting the title and description and the url of the news so that we can read it properly