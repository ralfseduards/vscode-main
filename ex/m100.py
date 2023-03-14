s = 'azcbobobegghakl'
alph = "abcdefghijklmnopqrstuvwxyz"
end = ""
prevLetter = s[0]
for letter in s:
    if alph.index(letter) < alph.index(prevLetter):
        end += " "
        end += letter
    else: end += letter
    prevLetter = letter
a = end.split(" ")
print(max(a, key=len))
