import sys

# ar binaaro meklseesanu!

def squareRoot(end:int):

    """guesses the square root"""

    lim = 0.000001
    min = 1.0
    max = end
    guess = (min+max) / 2
    count = 0

    while abs(end - guess**2) >= lim:
        count += 1
        if guess**2 > end:
            max = guess
        else:
            min = guess
        guess = (min+max) / 2
    print(f"\n\t\tsquare root of {end} is {guess}!  (guesses={count})\n")

def cubeRoot(end:int):

    """guesses the cube root"""

    lim = 0.000001
    min = 1.0
    max = end
    guess = (max+min) / 2
    counter = 0
    while abs(end - guess**3) > lim:
        if guess**3 > end:
            max = guess
        else:
            min = guess
        guess = (max + min) / 2 
        counter += 1 
    print(f"\n\t\tthe cube root of {end} is {guess}!  (guesses={counter})\n")


def newton_rapson(end:int):
    """the Newton - Rapson formula is the fastest way to find an approzimate root(square in this example)"""
    
    lim = 0.000001
    max = end 
    guess = max / 2
    count = 0

    while abs(guess**2 - max) >= lim:
        count += 1 
        guess = guess - ((guess**2 - max)/(2*guess))

    print(f"\n\t\tsquare root of {end} is {guess}!  (guesses={count})\n")

def main():
    try:
        x = int(input("input a number "))
        if sys.argv[1] == "square":
            squareRoot(x)
        elif sys.argv[1] == "cube":
            cubeRoot(x)
    except:
        print("\n\t\tSORRY IEVADI ARGV TERMINAALII\n")


    newton_rapson(x)


if __name__ == "__main__":
    main()