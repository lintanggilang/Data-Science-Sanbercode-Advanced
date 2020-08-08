from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as bs
import pandas as pd 

alamat = "https://pokemondb.net/pokedex/all"
safeAdd = Request(alamat, headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '\
    'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 '\
    'Safari/537.36'})
html = urlopen(safeAdd)
data = bs(html, 'html.parser')

table = data.find("table", {"id":"pokedex"})
rows = table.findAll("tr", limit = 29)
kolom = [i.text.replace('\n','') for i in rows[0].find_all('th')]

hasil = []
for row in rows[1:]:
    info = []
    for cell in row.findAll(["td", "th"]):
        info.append(cell.get_text().strip())
    hasil.append(info)

df = pd.DataFrame(hasil , columns=kolom)
#df.to_csv("pokedex.csv",index=False)
print(df.head())