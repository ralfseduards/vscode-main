def norm(x):
    return x * 10
x = 10
x = norm(x)
print(x)
# print(globals())

class Guys:
    def __init__(self, age, name):
        self.age = age
        self.name = name

boy = Guys(10, "Toma")
print(hasattr(boy, "name"))

print(hash(boy))

# help()

print(hex(69))

print(id(boy))

print(isinstance(boy, Guys))