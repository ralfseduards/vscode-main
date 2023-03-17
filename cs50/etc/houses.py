students = [
    {"name" : "hermione", "house" : "gryfindor"},
    {"name" : "harry", "house" : "gryfindor"},
    {"name" : "ron", "house" : "gryfindor"},
    {"name" : "draco", "house" : "slytherin"},
    {"name" : "padma", "house" : "ravenclaw"},
]

houses = set()
for student in students:
    houses.add(student["house"])

for house in sorted(houses):
    print(house)

    