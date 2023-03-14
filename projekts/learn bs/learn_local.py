from bs4 import BeautifulSoup

with open("projekts/dummy.txt" , "r") as f:
    file = f.read()
soup = BeautifulSoup(file, "html.parser")

body = soup.find_all("p")


# print(soup.get_text())#gets the text

# #also gets the text
# for i in body:
#     print(i.text)

# # finds all "a"s and gets the links out of them
# for i in soup.find_all("a"):
#     print(i.get('href'))


