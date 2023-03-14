"""think of a number from 0 and 100 and i will guess it"""

min = 0
max = 100
correct = False
guesses = 0

while not correct:
    guess = (min+max)/2
    print(f"\n\tIs your secret number {int(guess)}?\n")
    response = input("Enter 'h' to indicate the guess is too high. \
                      Enter 'l' to indicate the guess is too low. \
                     Enter 'c' to indicate I guessed correctly.")
    if response == "h":
        max = guess
    elif response == "l":
        min = guess
    elif response == "c":
        correct = True
    guesses += 1
    
print(f"\n\tGame over. Your secret number was: {int(guess)} !!! ({guesses} guesses)\n")
