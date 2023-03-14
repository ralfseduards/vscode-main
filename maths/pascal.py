import combina

#--------------------------------------

# printPascal() for printing
# makePascal() for returning

#--------------------------------------

def printPascal(lines:int):
    """prints the pascal's triangle, input amount of lines"""
    print("")
    l = ""
    firstBlank = lines - 1
    for line in range(lines):
        l += " " * firstBlank
        firstBlank -= 1

        for pos in range(line + 1):
            l += str(combina.comb(line, pos))
            l += " "
        print(l)
        l = ""
    print("")

def makePascal(lines:int):
    """returns the pascal's triangle, input amount of lines"""

    l = ""
    res = []
    for line in range(lines):

        for pos in range(line + 1):
            l += str(combina.comb(line, pos))
        res.append(l)
        l = ""
    return res

def main():
    try:
        lines = int(input("\nlines: "))
    except ValueError as ve:
        print(f"{ve} - \nIEVADI SKAITLI")
        exit()

    printPascal(lines)

    print(makePascal(lines))

if __name__ == "__main__":
    main()
