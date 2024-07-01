import requests
from send_email import send_email

topic = "tesla"
api_key = "cf0a9ad9170c42e8a851d22449ec2539"
url = f"https://newsapi.org/v2/everything?q=tesla&topic={topic}&sortBy=publishedAt&language=en&apiKey=cf0a9ad9170c42e8a851d22449ec2539"

# make request
request = requests.get(url)

# get dict with data
content = request.json()
print(content)


body = ""
# access article and description
for article in content['articles'][:10]:
    if article['title'] is not None and article['description'] is not None:
        body = "Subject: News Feed" \
               + "\n" + body + article['title'] + "\n" \
               + article['description'] \
               + "\n" + article['url'] + 2*"\n"

body = body.encode("utf-8")
# message = f"""\
# Subject: News Feed from Yahoo Finance
#
# Topics and Descriptions: {body}
# """
send_email(body)
