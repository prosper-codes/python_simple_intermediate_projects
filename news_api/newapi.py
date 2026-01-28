import requests
import  send_email

topic ="tesla"
api_key = "asdasd53"
url = "https://newsapi.org/v2/everything?"\
    f"q={topic}&"\
      "from=2025-12-28&sortBy=publishedAt&apiKey={apikey}&language=en"

requst=requests.get(url)
content=requst.json()
message=""
for article in content["articles"][:20]:
    if article["title"] is not None and article["description"] is not None:
        message += (
            "Subject: Today's news\n\n"  # Newline after subject
            f"{article['title']}\n"  # Newline after title
            f"{article['description']}\n"  # Newline after description
            f"{article['url']}\n\n"  # Extra newline after URL
        )



send_email.send_email(message)


