from urllib.request import urlopen
from bs4 import BeautifulSoup

alamat = "https://blog.sanbercode.com/"
html = urlopen(alamat)
data = BeautifulSoup(html, 'html.parser')


i=0
while(i<3):
    judul = (data.findAll("a", {"class":"text-dark"})[i]).get_text().replace("\n","")
    penulis = (data.findAll("a", {"class":"text-muted text-capitalize"})[i]).get_text().replace("\n","")
    print(judul + penulis)
    i+=1
    


# judul_1 = (data.findAll("a", {"class":"text-dark"})[0]).get_text().replace("\n","")
# judul_2 = (data.findAll("a", {"class":"text-dark"})[1]).get_text().replace("\n","")
# judul_3 = (data.findAll("a", {"class":"text-dark"})[2]).get_text().replace("\n","")

# Penulis_1 = (data.findAll("a", {"class":"text-muted text-capitalize"})[0]).get_text().replace("\n","")
# Penulis_2 = (data.findAll("a", {"class":"text-muted text-capitalize"})[1]).get_text().replace("\n","")
# Penulis_3 = (data.findAll("a", {"class":"text-muted text-capitalize"})[2]).get_text().replace("\n","")

# list_1 = [judul_1, Penulis_1]
# list_2 = [judul_2, Penulis_2]
# list_3 = [judul_3, Penulis_3]

# print(list_1)
# print(list_2)
# print(list_3)