# with decorators i can extend the functionality of a function without altering it.
# a single func can have multiple decorators

def nice(func):
    def wrap():
        print("\n============")
        func()
        print("============\n")
    return wrap

@nice #------------------------- "decorates the next function"
def print_text():
    print("Hello world!")


@nice
def print_me():
    print("memememememe")

# print_text = decor(print_text) # alter the original func by replacing it with a decorated one

print_text() ; print_me()


# nested funkcijas var accessot enclosing func variables
