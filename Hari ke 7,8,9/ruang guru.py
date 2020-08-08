# import tweepy
# import re
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np

# consumer_key = #
# consumer_secret = #
# access_token = #
# access_token_secret = #

# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
# api = tweepy.API(auth)


# search_words = "ruang guru"
# date_since = "2020-08-04"
# new_search = search_words + " -filter:retweets"

# tweets = tweepy.Cursor(api.search,
#         q=new_search,
#         lang="id",
#         since=date_since).items(100)

# items = []
# for tweet in tweets:
#     item = []
#     item.append (' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet.text).split()))
#     #items.append(item)
#     items.append(item)
# hasil = pd.DataFrame(data=items, columns=['tweet'])
# print(items)
# print(hasil)

# pos_list= open("kata_positif.txt","r")
# pos_kata = pos_list.readlines()
# neg_list= open("kata_negatif.txt","r")
# neg_kata = neg_list.readlines()


# # #Total Nilai = Nilai Positif - Nilai Negatif

# # S=[]
# # positif=[]
# # negatif=[]
# # for item in items:
# #     count_p = 0
# #     count_n = 0
# #     for kata_pos in pos_kata:
# #         if kata_pos.strip() in item[0]:
# #             count_p +=1
# #     for kata_neg in neg_kata:
# #         if kata_neg.strip() in item[0]:
# #             count_n +=1
# #     print ("positif: "+str(count_p))
# #     print ("negatif: "+str(count_n))
# #     print ("----")
# #     positif.append(count_p)
# #     negatif.append(count_n)
# #     S.append(count_p - count_n)
# #     # print ("-----------------------------------------------------")
    
# # hasil = pd.DataFrame(data=items, columns=['tweet'])
# # print(hasil)

# # hasil["value"] = S
# # print ("Nilai rata-rata: "+str(np.mean(hasil["value"])))
# # print ("Standar deviasi: "+str(np.std(hasil["value"])))

# # # labels, counts = np.unique(hasil["value"], return_counts=True)
# # # plt.bar(labels, counts, align='center')
# # # plt.gca().set_xticks(labels)
# # # plt.show()