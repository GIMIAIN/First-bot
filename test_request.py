import requests
from newsapi import NewsApiClient

news_api_key='fa13a787efc342cd9aeaeedce800e82a'

url = ('https://newsapi.org/v2/everything?'
       'q=Apple&'
       'from=2022-04-09&'
       'sortBy=popularity&'
       'language=ru&'
       'page=1&'
       'apiKey='+news_api_key)

response = requests.get(url).json()["articles":"title"]

print(response)