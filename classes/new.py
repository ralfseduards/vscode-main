def romanToInt(s: str) -> int:
    d = {
        "I": 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }
    
    res = 0
    value = lambda x : d.get(s[x])
    skipped = False
    i = 0
    if len(s) <1:
        for i in range(len(s)-1):
            if skipped:
                skipped = False
                continue
            if value(i) >= value(i+1):
                res += value(i)
            else: 
                res += value(i+1) - value(i)
                skipped = True
        
        if not skipped:
            res += value(i+1)
    else: res += d.get(s)
    return res

print(romanToInt(input()))