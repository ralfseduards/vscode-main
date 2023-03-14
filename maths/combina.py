def fact(a):
    """calculates the factorial"""
    res = 1
    for i in range(1, a + 1):
        res *= i
    return res


def comb(n, k):
    """calculates the combination"""
    return fact(n) // ((fact(k)) * (fact((n - k))))


if __name__ == "__main__":
    print(comb(7, 4))
