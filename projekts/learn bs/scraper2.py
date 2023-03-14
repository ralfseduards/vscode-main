import requests
from bs4 import BeautifulSoup

#scrapin the soup
url = "https://beautiful-soup-4.readthedocs.io/en/latest/#"
request = requests.get(url)
soup = BeautifulSoup(request.content, "html.parser")

def str_func():
    tags = soup.find_all("h2", class_="title is-5", string=lambda text: "python" in text.lower())
    dct = {}
    for tag in tags:
        pass

with open("projekts/learn bs/bs.txt", "w") as f:
    body = soup.find(role="main")
    f.write(str(body.get_text()))
    print(body.get_text())