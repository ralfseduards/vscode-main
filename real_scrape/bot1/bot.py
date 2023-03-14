import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

headers = {"Accept-language": "en-US, en;q=0.5"} # anglu valodaa
url ="https://www.imdb.com/search/title/?groups=top_1000&ref=add_prv"

result = requests.get(url, headers=headers)
soup = BeautifulSoup(result.content, "html.parser")

# initialize storage!

titles = []
years = []
time = []
imdb_ratings = []
metascores = []
votes = []
us_gross = []

box = soup.find_all(class_="lister-item mode-advanced")

for container in box:
    name = container.h3.a.text
    titles.append(name)

    year = container.h3.find("span", class_="lister-item-year text-muted unbold").text
    years.append(year)

    runtime = container.p.find("span", class_="runtime").text
    time.append(runtime)

    rating = container.strong.text.strip()
    imdb_ratings.append(float(rating))

    meta = container.find("span", class_="metascore").text if container.find("span", class_="metascore") else "-"
    metascores.append(meta)

    nv = container.find_all("span", attrs={"name":"nv"})#jo vini abi ir span tagaa un viniem abiem name ir nv
    vote = nv[0].text
    votes.append(vote)

    gross = nv[1].text if len(nv)>2 else "-"
    us_gross.append(gross)


# making a dataframe
movies = pd.DataFrame({
    "movie" : titles,
    "year" : years,
    "length" : time,
    "imdb" : imdb_ratings,
    "metascore" : metascores,
    "vote" : votes,
    "gross" : us_gross
    })
# print(movies.dtypes)
# jaasatiira data!!

# cleaning the data
movies["year"] = movies["year"].str.extract("(\d+)").astype(int)
movies["length"] = movies["length"].str.extract("(\d+)").astype(int)
movies["metascore"] = movies["metascore"].astype(int)
movies["vote"] = movies["vote"].str.replace(",", "").astype(int)
# gross ir sarezgits jo tam jaatnem elementi no abam pusem
movies["gross"] = movies["gross"].map(lambda x: x.lstrip("$").rstrip("M"))
# un jaaparveido par float, apgruutina tas, ka ir rows kuros nav values
movies["gross"] = pd.to_numeric(movies["gross"], errors="coerce")
# Nan ir float!!

# movies.to_csv("movies.csv")
print(movies[movies["year"] <=2000].sort_values("imdb", ascending=False).head(5).reset_index())
