# import tweepy

# consumer_key = "lyZKaT5zqqDiAZhnqwOjnIV8M"
# consumer_secret = "AUXB6WEf8OAd6EjgZrnQd32XDcWVAcjn7VN5BQWsHbuk3C5fq2"
# access_token = "1288268575870836736-LdlLELoIYdfkcuhkCepASV9NPcVEFb"
# access_token_secret = "s5nAYl7dgns0izv1olo8NV9HabSv8NnyQavVrGHuKV7L0"

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