# import tweepy

# consumer_key = #
# consumer_secret = #
# access_token = #
# access_token_secret = #

# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
# api = tweepy.API(auth)

# def user():
#     nama = "jokowi"
#     jumlah = 200
#     hasil = api.user_timeline(id=nama, count=jumlah)
#     for tweet in hasil:
#         print(tweet.text)
#         print("----------------------------------------")


# twit = []
# def test():
#     nama = "jokowi"
#     jumlah = 200
#     hasil = api.user_timeline(id=nama, count=jumlah)
#     for tweet in hasil:
#         twit.append(tweet.text)
#     #print(twit)

#     print("---------------------------------")

#     keyword = ["covid", "virus"]
#     list = []
#     for i in twit:
#         for x in keyword:
#             if x in i.lower():
#                 list.append(i)

#     print(list)
#     print(len(list))
# test()

# print("done")