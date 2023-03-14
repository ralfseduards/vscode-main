import random

target = str(random.randint(0,9999))
guess = input("your guess: ")
cows = 0
bulls = 0
guessses = 0

while target != guess:
    for num in enumerate(target): # use enumerate instead of range(len())
        if guess[num[0]] == target[num[0]]:
            cows += 1
        else:
            bulls += 1
    print(f"{cows} cows, {bulls} bulls")
    cows = 0
    bulls = 0
    count = 0
    guess = input("your guess: ")

print("moooooooooooooooooooooooooooooo")


