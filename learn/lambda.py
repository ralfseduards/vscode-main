
# lambda (jebcik variables): (1 funkcija)
b = lambda a: a*4
print(b(4))

def kaapinaat(x : int, n:int):
    return lambda x, n  : x**n
a = kaapinaat(5,6)
print(a(2,3))


def my_func(f, arg):
    return f(arg)

print(my_func(lambda x: 2*x*x, 5))

print("divi ceturtajaa", (lambda x: x**4) (2))