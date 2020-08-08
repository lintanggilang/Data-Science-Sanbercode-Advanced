from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd 

#############################################################################################################################

# alamat = "https://en.wikipedia.org/wiki/List_of_brightest_stars"
# html = urlopen(alamat)
# data = BeautifulSoup(html, 'html.parser')


# table = data.findAll("table", {"class":"wikitable"})[0].tbody

# rows = table.findAll("tr")

# kolom = [i.text.replace('\n','') for i in rows[0].find_all('th')]

# hasil = []
# for row in rows[1:]:
#     info = []
#     for span in row.findAll(["span"]):
#         span.decompose()
#     for cell in row.findAll(["td", "th"]):
#         info.append(cell.get_text().strip())
#     hasil.append(info)

# df = pd.DataFrame(hasil , columns=kolom)
# print(df)


#############################################################################################################################
#############################################################################################################################

alamat2 = "https://en.wikipedia.org/wiki/List_of_action_films_of_the_2020s"
html2 = urlopen(alamat2)
data2 = BeautifulSoup(html2,'html.parser')


film = pd.read_html("https://en.wikipedia.org/wiki/List_of_action_films_of_the_2020s")[1]

film_dict = film.to_dict() 
print(film_dict)

print("#############################################################################################################################")
print(film_dict.keys())
# print("#############################################################################################################################")
# print(film_dict['Title'])
# print("#############################################################################################################################")
# print(film_dict['Director'])
# print("#############################################################################################################################")
# print(film_dict['Cast'])
# print("#############################################################################################################################")
# print(film_dict['Country'])
# print("#############################################################################################################################")
# print(film_dict['Subgenre/notes'])
# print("#############################################################################################################################")
# print(film_dict['Unnamed: 5'])
# print("#############################################################################################################################")
# print(film_dict['Unnamed: 6'])
# print("#############################################################################################################################")
del film_dict['Unnamed: 5'] 
del film_dict['Unnamed: 6'] 
print(film_dict.keys())
print("#############################################################################################################################")
print(film_dict)
print("#############################################################################################################################")
print("#############################################################################################################################")
film_list=list(film_dict.values())
print(film_list)

# i=0
# hasil2 = []
# while (i<2):
#     table2 = data2.findAll("table", {"class":"wikitable sortable"})[i]
#     rows2 = table2.findAll("tr")
#     for row2 in rows2[2:]:
#         for cell in row2.findAll("a"):
#             info = cell.get_text()
#         hasil2.append(info)
#     i+=1

# print(hasil2)
