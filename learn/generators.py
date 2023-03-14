# a type of iterable
# cannot be indexted but can be iterated over with for loops
# can be created using functions + yield statement

# used to work with large datasets!!

# vins printeejas jociigs jo vins nestoro values in memory - generator superpower

# generator comprehension izmanto round brackets


def countdown():
    i = 5
    while i > 0:
        yield i
        i -= 1


print("\n", countdown(), "\n")
for i in countdown():
    print(i)
print("")
# ar vinu taisa infinite sequances


def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1


gen = infinite_sequence()
print(next(gen))
print(next(gen))

# --------------------------------------- prime numbers (...all of them)

import itertools


def prime():
    # 2 ir izneemums
    yield 2
    primes_cache = [2]
    # loop over positive , odd ints

    for n in itertools.count(3, 2):
        # assume that n is prime
        is_prime = True

        # jaachecko vai n ir divisible ar kaaadu skaitli no cache

        for p in primes_cache:
            if n % p == 0:
                is_prime = False
                break
        # ja visi primes ir izmeeginaati, tad n ir prime

        if is_prime:
            primes_cache.append(n)  # pievieno cache
            yield n  # pievieno generator


for prime in prime():
    print(prime)
    if prime > 200:
        break

# --------------------------------------- generator expressions

squares = (x**2 for x in itertools.count(1))

for i in squares:
    print(i)
    if i > 100:
        squares.close()

import sys


print("bytes:", sys.getsizeof(squares))


# use generators!!!
