# library yang digunakan
from urllib.request import urlopen
from bs4 import BeautifulSoup


alamat = "https://blog.sanbercode.com/"
html = urlopen(alamat)
data = BeautifulSoup(html, 'html.parser')

list1 = []
list2 = []
blok = data.findAll("div", {"class":"mt-3 mt-md-0 mb-3 d-flex post_box_style3"})

for p in blok:
    judul = p.find('a', {'class':'text-dark'}).get_text().strip()
    penulis = p.find('a', {'class':'text-muted text-capitalize'}).get_text().strip()
    list1.append(judul)
    list2.append(penulis)

print(list1)
print(list2)