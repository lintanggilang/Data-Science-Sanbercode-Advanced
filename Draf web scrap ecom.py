from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as bs
import pandas as pd 

print("start-1")

alamat = "https://www.tokopedia.com/search?st=product&q=phone"
safeAdd = Request(alamat, headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '\
    'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 '\
    'Safari/537.36'})
html = urlopen(safeAdd)
data = bs(html, 'html.parser')

print("start -2")

#UPDATE
items = data.findAll("div",{"class":"css-1g20a2m"})
print(len(items))

print("start-2")

kolom_judul = []
kolom_harga = []

#UPDATE
for item in items:
    judul = item.find("div",{"class":"css-18c4yhp"}).get_text()
    harga = item.find("div",{"class":"css-rhd610"}).get_text()
    kolom_judul.append(judul)
    kolom_harga.append(harga)

df = pd.DataFrame(list(zip(kolom_judul, kolom_harga)), columns =['Barang', 'Harga']) 

print(df.head())

print("---------------------------")
print("done")