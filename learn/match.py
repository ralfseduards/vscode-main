a = "1"


match a:
    case 777:
        print("ir septini")
    case 666:
        print("ir sesi")
    case 1|2|3|5|6|7|8|9:
        print("not allowed")
    case _ :
        print("nebija match")

print("")

x = int(input("ievadi x veertiibu: "))
y = int(input("ievadi y veertiibu: "))
print("")

koord = (x,y)

match koord:
    case (0,0):
        print("saakumpunkts")
    case (0,b):
        print(f"y={b}")
    case (a,0): 
        print(f"x={a}")
    case (a,b):
        print(f"x={a}, y={b}")
print("")

print(a,b)  #case var assignot variable!! 

# niiiice