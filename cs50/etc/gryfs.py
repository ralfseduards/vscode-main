students = [
    {"name" : "harry", "house" : "gryfindor"},
    {"name" : "hermione", "house" : "gryfindor"},
    {"name" : "ron", "house" : "gryfindor"},
    {"name" : "draco", "house" : "slytherin"},
]

gryfindors = [
    student["name"] for student in students if student["house"] == "gryfindor"
]

print(gryfindors)