**classes**
*) classes are used to make objects

    Classes allow us to logically group data and functions in a way that makes them easy to use and to alter.

A class is a BLUEPRINT for an instance of that class
-DEFINITIONS

1. methods - functions associated with a class
2. instances - an instance of a class (each instance is unique)
3. instance variables - contain data that is unique to each instance
4. __init__(self) - the initialization method (pienemts iekavaas rakstiit self)
__init__ always runs first
5. class variables - the same for the whole class ...what kind of data would we want to be shared over all instances?
6. alternative constuctor - a method that provide a different way to init instances


-Types of variables:
    a.instance
    b.class

-Types of methods:
    a. regular - automaticaly take the instance as the first variable
    b. class - recieve the class as the first argument (class variable convention - "cls")
        @classmethod
    c. static - dont pass anything automatically(just like basic functions but we group them in a class for conveniance)
        @satic method

inheritance - allows to inherit attributes and methods from a mother class

2 python funcs:
    1. isinstance - is the object an instance of the class
    2. issubclass - tells if a class is a subclass of another


Magic methods - dunder (double underscore) methods

Can create a method that allows to change the built in ones (__add__, __abs__, __len__...)

1.
@property - decorates a method so that it can be acessed as a variable (A GETTER)
- the method itself returns something
2.
@{name of the method}.setter
def {name of the same method}(self, new variable):
    ...
- a setter is used to change (set) the value of a property object
- a setter is aactivated by assigning something
3.
@{name of the method}.deleter
def {name of the same method}(self): - takes just the "self", because it just need to delete a value
    ...

>>>del instance.property