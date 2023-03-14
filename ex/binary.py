"""converts a decimal number into binary"""
def dec_bin():

    num = int(input("give me a number: "))
    cache = num
    if num < 0:
        Neg = True
        num = abs(num)
    else: Neg = False

    result = ""
    if num == 0:
        result = "0"
    while num > 0:
        result = str(num%2) + result
        num = num // 2
    if Neg:
        result = "-" + result

    print(f"binary of {cache} --> {result}")


dec_bin()