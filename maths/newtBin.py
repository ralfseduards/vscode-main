import pascal
import re

def getBin(a:int,b:int,n:int):

    """returns the newtons binome for the variables (a + b) ^ n ~~ in string format"""

    res = []
    bN = 0
    aN = n
    for i in pascal.makePascal(n)[n-1]:
        res.append( f"{i}*({a}^{aN})*({b}^{bN})" ) 
        aN -= 1
        bN += 1
    joined = " + ".join(res)
    return joined

def getK():
    pass

def main():
    i = input("ievadi binomu(a+b): ")
    n = int(input("kādā pakāpē?: "))
    regex = re.search(r"(\d+)\+(\d+)", i)

    print(getBin(int(regex.group(1)), int(regex.group(2)), n))


if __name__ == "__main__":
    main()

