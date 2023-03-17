import re

email = input("whats yout email? ")

if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, flags=re.IGNORECASE):
    print("valid")
else: print("invalid!")
