# number guessing game
from random import randint

the_number = randint(1, 100)
correct = False

while not correct:
    try:
        guess = int(input("Enter your guess..."))
    except ValueError:
        continue
    if guess < the_number:
        print(f"Your guess of {guess} is TOO LOW")
    elif guess > the_number:
        print(f"Your guess of {guess} is TOO HIGH")
    else:
        print(f"Your guess is CORRECT!!, the number was {the_number}")
        correct = True
