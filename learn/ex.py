def decor(func):
    def wrap(*args):
        print("\n----------")
        print(func(*args))
        print("----------\n")
    return wrap

@decor
def one(a):
    return a + 1

one(1)


