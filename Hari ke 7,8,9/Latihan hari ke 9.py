# import tweepy
# import re
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np

# consumer_key = "lyZKaT5zqqDiAZhnqwOjnIV8M"
# consumer_secret = "AUXB6WEf8OAd6EjgZrnQd32XDcWVAcjn7VN5BQWsHbuk3C5fq2"
# access_token = "1288268575870836736-LdlLELoIYdfkcuhkCepASV9NPcVEFb"
# access_token_secret = "s5nAYl7dgns0izv1olo8NV9HabSv8NnyQavVrGHuKV7L0"

# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
# api = tweepy.API(auth)


# search_words = "jouska"
# date_since = "2020-07-25"
# new_search = search_words + " -filter:retweets"

# tweets = tweepy.Cursor(api.search, q=new_search, lang="id", since=date_since).items(50)

# items = []
# for tweet in tweets:
#     item = []
#     item.append (tweet.user.screen_name)
#     item.append (tweet.user.location)
#     item.append (' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet.text).split()))
#     items.append(item)
# hasil = pd.DataFrame(data=items, columns=['user','lokasi','tweet'])
# #print(hasil)

# json_data = hasil.to_json(orient='split')
# print(json_data)
