# https://realpython.com/python-hash-table/

# there is a subtle difference between hash tables and dictionaries
# dictionary ir kaa funkcija - katram key ir tikai viens value
# the hash() function returns different values every time you run it(as a security measure),
# but values of equal objects do have equal values (its is deterministic)
print(hash("abcd"))
print(hash("abcd"))

