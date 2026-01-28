import requests
import  send_email
api_key = "f2839e9b26684752902f2a640b76e153"
url = "https://newsapi.org/v2/everything?q=tesla&from=2025-12-28&sortBy=publishedAt&apiKey=f2839e9b26684752902f2a640b76e153"

requst=requests.get(url)
content=requst.json()
message=""
for article in content["articles"]:
    if article["title"] is not None and article["description"] is not None:
        message = message+article["title"] + "\n" + article["description"] + 3*"\n"


message=message.encode("utf-8")
send_email.send_email(message)



