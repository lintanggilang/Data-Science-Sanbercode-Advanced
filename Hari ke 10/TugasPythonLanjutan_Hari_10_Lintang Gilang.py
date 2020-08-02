from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as bs
import pandas as pd 

import numpy as np
import matplotlib.pyplot as plt 
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler


alamat = "https://pokemondb.net/pokedex/all"
safeAdd = Request(alamat, headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '\
    'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 '\
    'Safari/537.36'})
html = urlopen(safeAdd)
data = bs(html, 'html.parser')

table = data.find("table", {"id":"pokedex"})
rows = table.findAll("tr", limit = 17)
kolom = [i.text.replace('\n','') for i in rows[0].find_all('th')]

hasil = []
for row in rows[1:]:
    info = []
    for cell in row.findAll(["td", "th"]):
        info.append(cell.get_text().strip())
    hasil.append(info)

df = pd.DataFrame(hasil , columns=kolom)

#df.to_csv("pokedex.csv",index=False)
df.to_excel("TugasPythonLanjutan_Hari_10_Lintang Gilang.xlsx")
print(df.head())
print("done")

##########################################################################################################################################

# #Kesimpulan

# # 	    Attack	    Defense	    kluster
# # count	984.000000	984.000000	984.000000
# # mean	79.696138	74.101626	2.438008
# # std	32.327988	30.830351   1.290161
# # min	5.000000	5.000000    0.000000
# # 25%	55.000000	50.000000   1.000000
# # 50%	75.000000	70.000000   3.000000
# # 75%	100.000000	90.000000	4.000000
# # max	190.000000	230.000000	4.000000

# # Berdasarkan data pokedex terdapat sebanyak 985 pokemon dengan no id 1 sd 850 
# # Diketahui bahwa rata-rata Attack pokemon berikisar 47 sd 111 yaitu sebanyak 680 pokemon atau 69%
# # Diketahui bahwa rata-rata Defense pokemon berikisar 44 sd 104 yaitu sebanyak 699 pokemon atau 71%

# # Rekomendasi Pokemon yang sebaiknya di tangkap adalah pokemon yang memiliki Attack > 111 dan Defense > 104

# #Berikut List Pokemon yang sebaik nya di Tangkap
# # Charizard Mega Charizard X	# Donphan	                # Hippowdon	                # Diancie Mega Diancie
# # Golem	                        # Tyranitar	                # Abomasnow Mega Abomasnow	# Wishiwashi School Form
# # Golem Alolan Golem	        # Tyranitar Mega Tyranitar	# Rhyperior	                # Golisopod
# # Kingler	                    # Swampert Mega Swampert	# Dialga	                # Tapu Bulu
# # Rhydon	                    # Aggron Mega Aggron	    # Regigigas	                # Solgaleo
# # Pinsir Mega Pinsir	        # Salamence Mega Salamence	# Arceus	                # Buzzwole
# # Gyarados Mega Gyarados	    # Metagross	                # Gigalith	                # Kartana
# # Kabutops	                    # Metagross Mega Metagross	# Escavalier	            # Necrozma Dusk Mane Necrozma
# # Steelix Mega Steelix	        # Groudon	                # Zekrom	                # Necrozma Dawn Wings Necrozma
# # Scizor Mega Scizor	        # Groudon Primal Groudon	# Tyrantrum	                # Stakataka
# # Heracross Mega Heracross	    # Garchomp Mega Garchomp	# Avalugg	                # Melmetal

# print("penggemar pokemon")



