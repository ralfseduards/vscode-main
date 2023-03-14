# map and filter are very useful higher order functions
# map takes a function and an iterable and aplies the function to each value

nums = [11,22,33,44,55]

def do_map():

    result = list(map(lambda x: x +5, nums))
    print(result)

# filter iterates through the iterable and returns onyl the values that match a condition (predicate)

def do_filter():

    result = list(filter(lambda x : x%2==0, nums))
    print(result)

do_filter()
