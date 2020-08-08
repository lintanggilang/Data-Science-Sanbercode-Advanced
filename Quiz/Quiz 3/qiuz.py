from bs4 import BeautifulSoup

markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup)
a_tag = soup.a

i_tag = soup.i.extract()

# a_tag
# # <a href="http://example.com/">I linked to</a>

# i_tag
# # <i>example.com</i>

# print(i_tag.parent)

print("done")
