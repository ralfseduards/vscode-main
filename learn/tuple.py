# iekavas vai nekas!!!
a = 1,2,3,4,5
print("\n", type(a), end="\n\n")


def pakaapes(x):
    return (2**i for i in range(1,x+1)) # return tuple


a, *b = pakaapes(4)

print(a,b)

if 4 in pakaapes(1):
    print("nice")
else: print("bozo")


