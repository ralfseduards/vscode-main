def hi(x):
    for i in range(x):
        yield i
a = hi(1000)
print(list(a))