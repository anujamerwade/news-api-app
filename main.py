import requests

api_key = "cf0a9ad9170c42e8a851d22449ec2539"
url = "https://newsapi.org/v2/everything?q=tesla&from=2024-05-28&sortBy=publishedAt&apiKey=cf0a9ad9170c42e8a851d22449ec2539"

# make request
request = requests.get(url)

# get dict with data
content = request.json()

# access article and description
for article in content['articles']:
    print(article['title'])
    print(article['description'])
