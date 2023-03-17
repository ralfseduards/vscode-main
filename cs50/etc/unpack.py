def f(*args, **kwargs):
    print("named: ", kwargs)

f(100,50,20, galleons = 30, sickles = 9)