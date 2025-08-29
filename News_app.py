import requests
import json

search = input("Search for the news here: ")
response = requests.get(f"https://newsapi.org/v2/everything?q={search}&from=2025-07-29&sortBy=publishedAt&apiKey=58b04830080d43ad99c2c52672d4bef5")
news = json.loads(response.text)
for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print(article["url"])
    print("-----------------------------------------")