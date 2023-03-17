import re

name = input("whats your name? ").strip()
# try to find the reverse 
if matches := re.search(r"^(.+), *(.+)$", name):
    name = f"{matches.group(2)} {matches.group(1)}"

print(f"Hello, {name}")