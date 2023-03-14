
cities = ['New York', 'Beijing', 'Cairo', 'Mumbai', 'Mexico']

for index, city in enumerate(cities,100): # enumerate returns a tuple with the index + element
    print(f"{index} : {city}") # unpacking the tuple


# find the index
one_city = "New YOrk"
if one_city in cities:
    idx = cities.index(one_city)
    print("\n", f"{one_city} has an index of {idx}" , sep = "")
else: 
    print("\n", f"{one_city} does not exist", sep = "")

# map() - iterates over all elements of the list, aplies a function to each

bonuses = [100, 50, 75]

iterator = map(lambda a: a*2, bonuses)
# map makes an iterator
print(list(iterator))


# filter() !!!!! - filter(fn, list)

scores = [70, 60, 80, 90, 50]

end = filter(lambda score : score >= 70, scores)

print(list(end))



countries = [
    ['China', 1394015977],
    ['United States', 329877505],
    ['India', 1326093247],
    ['Indonesia', 267026366],
    ['Bangladesh', 162650853],
    ['Pakistan', 233500636],
    ['Nigeria', 214028302],
    ['Brazil', 21171597],
    ['Russia', 141722205],
    ['Mexico', 128649565]
]

e = filter( lambda country: country[1] > 300_000_000, countries)
print("\n\n",tuple(e),sep = "")