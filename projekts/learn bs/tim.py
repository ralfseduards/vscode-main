from bs4 import BeautifulSoup
import re

with open("projekts/learn bs/tim.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

# tag = doc.find("option")
# # changes an attribute
# tag["value"] = "new value"
# # can add an atribute
# tag["color"] = "blue"
# print(tag.attrs) # prints a dict of variables
# print(tag) 

# #i can find multiple tags
# tag = doc.find_all(["p", "div", "li"])
# print(tag)

# # i can specify attribute of a tag
# tags = doc.find_all("option", text="Undergraduate", value="undergraduate")
# print(tags)

# # finding a specific class can be very important
# tags = doc.find_all(class_="btn-item")
# print(tags)

# # regular expressions!!
# tags = doc.find_all(string=re.compile("\$.*"), limit=1) # can limit the responses
# for tag in tags:
#     print(tag.strip())

tags = doc.find_all("input", type="text")
for tag in tags:
    tag["placeholder"] = "i changed you"

with open("changed.html", "w") as f:
    f.write(str(doc))