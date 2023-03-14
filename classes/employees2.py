class Employee:

    def __init__(self,first,last):
        self.first = first
        self.last = last
    
    @property
    def _email(self):
        return f"{self.first}.{self.last}@email.com"

    @property
    def _fullname(self):
        return f"{self.first} {self.last}"
    
    @_fullname.setter
    def _fullname(self, name):
        first, last = name.split()
        self.first = first
        self.last = last

    @_fullname.deleter
    def _fullname(self):
        print("delete name")
        self.first = None
        self.last = None



emp1 = Employee("John", "Smith")

emp1._fullname = "Big Joe"

print(emp1.first)
print(emp1._email)
print(emp1._fullname)

del emp1._fullname

print(emp1.__dict__)