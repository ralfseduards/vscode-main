# functions calling themselves

def factorial(i):
    if i == 1:
        yield 1 # base case (kaa stops) - vienaadiba kuru var izreekinaat neizmantojot recursion
    else:
        yield i * factorial(i-1)
    

def is_even(x):
    
    if x == 0:
        return True
    else: return is_odd(x-1)
def is_odd(x):
    return not is_even(x)

print(is_even(2))


