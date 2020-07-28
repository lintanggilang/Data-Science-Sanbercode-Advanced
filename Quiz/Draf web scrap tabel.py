from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as bs
import pandas as pd 

alamat = "https://en.wikipedia.org/wiki/List_of_Academy_Award-winning_films"
safeAdd = Request(alamat, headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '\
    'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 '\
    'Safari/537.36'})
html = urlopen(safeAdd)
data = bs(html, 'html.parser')

table = data.find("table", {"class":"wikitable sortable"})
rows = table.findAll("tr")

kolom = [i.text.replace('\n','') for i in rows[0].findAll('th')]

hasil = []
for row in rows[1:]:
    info = []
    for cell in row.findAll(["td", "th"]):
        info.append(cell.get_text().strip())
    hasil.append(info)
    
df = pd.DataFrame(hasil , columns=kolom)
df_2019 = df[df.Year.eq("2019")]
df_2019.to_csv("tugs1.csv",index=False) 
print(df_2019)