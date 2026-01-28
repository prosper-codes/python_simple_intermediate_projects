import requests

api_key = "f2839e9b26684752902f2a640b76e153"
url = "https://newsapi.org/v2/everything?q=tesla&from=2025-12-28&sortBy=publishedAt&apiKey=f2839e9b26684752902f2a640b76e153"

requst=requests.get(url)
content=requst.json()
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
