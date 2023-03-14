
class Employee:
    
    raise_amount = 1.25
    num_employees = 0

    def __init__(self, first, last, pay): # self is an instance; first, last, pay - arguments
        self.first = first 
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.num_employees += 1 # pie katra employee num palielinaas par 1

    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', '{self.pay}')"
    
    def __str__(self):
        return f"{self.fullname()} - {self.email}"
    
    def __add__(self,other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullname())

    def fullname(self): # vajag tikai self jo selfaa ieksaa jau ir initializoti argumenti
        return f"{self.first} {self.last}"
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) # or Employee.raise_amount

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_string): # alternative constructor
        first, last, pay = emp_string.split("-")
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() < 5:
            return True
        return False
    

class Developer(Employee):
    raise_amount = 1.5
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay) #!!!
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp not in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for employee in self.employees:
            print("-->", employee.fullname())



emp_1 = Developer("bob", "bobber", 100, "Python")
emp_2 = Developer("test", "user", 200, "java")

mg_1 = Manager("Sue", "Smith", 3000, [emp_1])


# print(issubclass(Developer, Manager))



# print(emp_1.pay)
# emp_1.apply_raise() # applyo Developer class raise, jo emp_1 ir Developer class instance 
# print(emp_1.pay)


# print(emp_1.__dict__)
# print(Employee.__dict__)


# print(emp_1.fullname)
# print(emp_1.fullname()) # jaaktivizee method (funkcija)
# print(Employee.fullname(emp_1)) #dara tiesi to pasu

# print("\n\n",  Employee)

#--------------------------------------------------
# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)
#---------------------------------------------------
# print(emp_1.__dict__)
# print(Employee.__dict__)
# print("")
# Employee.raise_amount = 1.30 # class variables var mainiit visaa class
# emp_1.raise_amount = 1.5 # vai tikai vienaa instance 
# print(emp_1.__dict__) # instance dict paraadaaas unikaalais variable

# Employee.set_raise_amt(1.01)

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

#--------------------------------------------------- class method


# emp_str_1 = "John-Doe-70000"
# emp_str_2 = "Steve-Smith-60000"
# emp_str_3 = "Jane-Doe-100"


# new_emp_1 = Employee.from_string(emp_str_1)

# print(new_emp_1.email)
# print(new_emp_1.pay)

#--------------------------------------------------- static method

# import datetime

# the_date = datetime.date(2023, 2, 15)

# print(Employee.is_workday(the_date))

#--------------------------------------------------- magic methods
print(emp_1)
print(emp_1 + emp_2)

print("tet".__len__())
print(len(emp_1))
