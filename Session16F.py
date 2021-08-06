import requests
import json

api_key = "31c21508fad64116acd229c10ac11e84"
url = "https://newsapi.org/v2/top-headlines?country=in&apiKey={}".format(api_key)

print(url)

response = requests.get(url)
# print(response)
# print(response.text)
# print(type(response.text)) # JSON (java Script Object Notation)

data = json.loads(response.text)
# print(data)
print(type(data))

print("TOTAL RESULTS:", data['totalResults'])
articles = data['articles']

for article in articles:
    print(article['author'])
    print(article['title'])
    print("~~~~~~~~~~~~~~~~~~~~~~~")
    print()