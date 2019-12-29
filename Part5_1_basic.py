import os
import tweepy as tw
import pandas as pd
import preprocessor.api as p
from preprocessor.api import clean, tokenize, parse

consumer_key = 'jLxo1SiAFioQcMnoN1GpZyPuz'
consumer_secret = 'IegW1T5CHHdCuYcXZ22KkTaB4guPhlSYMfYo08V3qpsRz9fW8I'

access_token = '1207488370' \
               '793803776-94axpEv4ohepsWWJl2LKVu5eBJWXLi'
access_token_secret = '6y6JHftCeeHoxwp2elb2zAphcbCNrk5hoseXYBBQPMRgw'

# perform authentication
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create our twitter api to access tweets from it
api = tw.API(auth)

search_words = "Korea"
date_since = "2019-11-16"

# Collect tweets
# 이 부분에 추가 정보를 통해 데이터 위치, 장소 등 설정 가능.
# tweepy.Cursor 메서드를 사용하면, pagination 이 자동 관리되어 100개 이상의 검색 결과를 가져올 수 있음
# # 모든 트위터 데이터가 검색되는 것은 아님(트위터사에서 이를 명시하고 있음)
# cursor = tweepy.Cursor(api.search,
#                        q=keyword,
#                        since='2015-01-01',  # 2015-01-01 이후에 작성된 트윗들로 가져옴
#                        count=100,           # 페이지당 반환할 트위터 수 최대 100
#                        geocode=location,    # 검색 반경 조건
#                        include_entities=True)
tweets = tw.Cursor(api.search,
              q=search_words,
              lang="en",
              since=date_since).items(5)
for tweet in tweets:
     print(tweet.text)
# Iterate and print tweets
for tweet in tweets:
     print(p.clean(tweet.text))