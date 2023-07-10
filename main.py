import random

def guess(x):
    randomNumber = random.randint(1,x)
    guess = 0
    while guess != randomNumber:
        guess = int(input("Guess a number between 1 and {} ".format(x)))
        print(guess)
        if guess<randomNumber:
            print("sorry too low")
        elif guess >randomNumber:
            print("Sorry guess again loo high")

    print("Congrats!")

guess(10)
