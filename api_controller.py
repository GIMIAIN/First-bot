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

response = requests.get(url).json()['articles']
'''
# Init
newsapi = NewsApiClient(api_key='fa13a787efc342cd9aeaeedce800e82a')

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='bitcoin',
                                          category='business',
                                          language='en',
                                          country='us')

# /v2/everything
''''''all_articles = newsapi.get_everything(q='bitcoin',
                                      from_param='2017-12-01',
                                      to='2017-12-12',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)''''''

# /v2/top-headlines/sources
sources = newsapi.get_sources()'''