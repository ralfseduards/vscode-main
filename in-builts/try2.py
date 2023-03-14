x = compile('print("hello")', "blablabla" , "eval")
exec(x)

a = complex(10)
print(a)

class Num:
    def __init__(self, value):
        self.value = value
x = Num(10)
print(x.value)
# delattr(x, "value")
setattr(x, "value", 3)
print(x.value)

print(dir(x))

print(divmod(10,3))
print(divmod(0,2))

array = ["pieci", "cetri", "triis", "divi", "viens"]
print(list(enumerate(array)))

b = 18
print(eval("b +      3"))

ls = [0,1,2,3,4,5,6,7,8,9]
print(list(filter(lambda x: x % 2 ==0, ls)))

form = 81
print(format(form, "c"))
print(format(form, "b"))

ls[9] = "end"
print(frozenset(ls))
ls[0] = "a"

print(getattr(x, "value"))