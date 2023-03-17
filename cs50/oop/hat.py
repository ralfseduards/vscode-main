import random

class Hat:
    houses = ["gryfindor", "hufflepuff", "slytherin", "ravenclaw"]

    @classmethod
    def sort(cls, name):
        print(f"{name} is in {random.choice(cls.houses)}")

Hat.sort("harry")