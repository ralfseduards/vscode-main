# *args izmanto ja nezin cik funcijaa buus variables
# *args must come after all named parameters

def f(pirmais, *ars):
    print(pirmais)
    print(ars)

f(1,2,3,4,5)
# *args returno tuple

#----------------------------
# **kwargs - keyword arguments (x = 2, y = 5 ...)

def my_func(x, y=7, *args, **kwargs):
    print(*kwargs)# ja kkam pieliek zvigzniiti tad ir string?
    print(kwargs)

my_func(2, 3, 4, 5, 6, a=7, b=8)
# **kwargs returno dict