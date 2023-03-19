import pdb
x = 11
y = 2

def okok(times):
    x = x * times
    y = y ** times
    return x, y
pdb.set_trace()
okok(3)
print(x,y)
print(okok(-2))