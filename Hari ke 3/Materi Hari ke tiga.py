from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd 

alamat = "https://en.wikipedia.org/wiki/List_of_brightest_stars"
html = urlopen(alamat)
data = BeautifulSoup(html, 'html.parser')


table = data.findAll("table", {"class":"wikitable"})[0].tbody

rows = table.findAll("tr")

kolom = [i.text.replace('\n','') for i in rows[0].find_all('th')]

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
#df.to_csv("test.csv", index=False)

######################################################################################################################################
### COBA COBA ###########################################

hasil = []
for row in rows[1]:
    print(row)
    for merge in row:
        print("*******")
    print("-----------------------------------------------------------------------")
#     info = []
#     for span in row.findAll(["span"]):
#         span.decompose()
#     for cell in row.findAll(["td", "th"]):
#         info.append(cell.get_text().strip())
#     hasil.append(info)



# print("rows :" , len(rows))
# print("row :" , len(row))
# print("cell :" , len(cell))
# print("kolom :" , len(kolom))

# print(row.get_text().strip())