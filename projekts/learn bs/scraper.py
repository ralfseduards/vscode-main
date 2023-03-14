import requests
from bs4 import BeautifulSoup as beautifulsoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)
soup = beautifulsoup(page.content, "html.parser") # izmanto page.content nevis page.text jo contents satur raw bytes



# narrows it down to the results container
results = soup.find("div", id="ResultsContainer")

# finds all jobs with python in it (makes a list)
python_jobs = results.find_all("h2", string=lambda text: "python" in text.lower())
# iterates over the list
for job in python_jobs:
    # finds the parent (card-content) of the job
    parent = job.parent.parent.parent
    #prints job
    print("-->" + job.text)
    # finds and prints company (only 1 in the card - so i use find)
    company = parent.find("h3", class_="subtitle is-6 company")
    print(company.text)
    # finds and prints location (only 1 in the card - so i use find)
    location = parent.find("p", class_="location")
    print(location.text + "\n")

    # finds all links in the parent
    links = parent.find_all("a")
    #iterates over the links
    for link in links:
        #checks if it is the "apply" link
        if link.text == "Apply":
            # prints the href attribute(link)
            print(f"Apply: {link['href']}!\n")

