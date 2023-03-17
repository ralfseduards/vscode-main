class Student:
    def __init__(self, name, house, patronous):
        self.name = name
        self.house = house #activates the setter (kas to be just .house to activate the property method)
        self.patronous = patronous
        
    def charm(self):
        match self.patronous:
            case "stag":
                return "🐴"
            case "otter":
                return "🦦"
            case "jack russel terrier":
                return "🐶"
            case _:
                return "🪄"

    def __str__(self):
        return f'-->{self.name} from {self.house}'


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        # we use property so that every time self.name is called (even in main), we check if its empty
        if not name:
            raise ValueError("name is missing!")
        self._name = name

    @property
    def house(self):
        return self._house
    # ^^technically the atrribute is called ._house, but the property is still called .house

    @house.setter
    def house(self, house):
        if house not in ["gryfindor", "hufflepuff", "slytherin", "ravenclaw"]:
            raise ValueError("invalid house")
        self._house = house

    @classmethod
    def get(cls):
        name = input("name: ")
        house = input("house: ")
        patronous = input("patronous: ")
        return cls(name, house, patronous)
    


def main():
    student = Student.get()
    student._house = "get cought"
    # properties dont work fully, but variables with _ shouldnt be used by convetion
    print(student)

if __name__ == "__main__":
    main()