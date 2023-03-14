'''''
number1 = 40
number2 = 30

if number1 * number2 <= 1000:
    print("the result is", number1 * number2)
else:
    print( "the result is",number1 + number2)
'''''

'''
n1 = 0
for i in range(10):
    print("current number", i,"previous number", n1, "sum:", n1+i)
    n1 = i
'''

'''
a = input()
print("og string is", a, "\n printing only even inde chars")

size = len(a)

for i in range(0, size, 2):
    print(f"index [{i}]", a[i])
'''

a = input("vaards:")
n = int(input("cik burti?:"))

def remove(a, n):
    new = a[n:]
    print(new)

if n < len(a):
    remove(a, n)
else:
    print("nawww")
