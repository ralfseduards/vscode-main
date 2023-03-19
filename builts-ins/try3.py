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
print(isinstance("BA", str))

print(locals() == globals())

guy = object()
print(dir(guy))

print(oct(69))
print(format(69, "o"))

print(ord("a"))

setattr(Guys, "girl", "her")
print(Guys.girl)

print(slice(9))
print(vars(Guys))


for item in zip([1,2,3], ["one" , "two" , "three"]):
    print(item)


