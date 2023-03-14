# an iterable has the ability to return its elements one at a time
# can be looped using a for loop

for i in range(1,3):
    print(i)

# an itereator is the agent that performs the iteration
# iter()

colors = ["red", "green", "blue"]
colors_iter = iter(colors)

# Once you have the iterator,
# you can get the next element from the iterable using the next() function

color = next(colors_iter)
print(color)

color = next(colors_iter)
color = next(colors_iter)
print(color)


carts = [('SmartPhone', 400),
         ('Tablet', 450),
         ('Laptop', 700)
         ]
tax = 0.1

carts = map(lambda item : [item[0], int(item[1]), int(item[1] * tax)], carts)

print(list(carts))