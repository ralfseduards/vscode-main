from bs4 import BeautifulSoup
import requests

url = "http://octopress.org/"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

all_a = list(map(lambda line: line.text, soup.find_all("a")))
print(all_a)

for i in soup.find_all("a"):
    if i.text == "Documentation":
        print(i.get("href"))
        print(i.parent.parent, "\n")

    if "deploy" in i.text:
        print(i.text)
        print(i.get("href"))

print(type(soup.get_text()))
