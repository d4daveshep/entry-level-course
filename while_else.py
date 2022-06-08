from random import random, randint

i = randint(1,10)  # get a random int between 1 and 10 inclusively

# while the int is high, keep generating more until we hit a low one
while i > 5:
    print(i, "high")
    i = randint(1, 10)  # get a random int between 1 and 10 inclusively
else:
    print(i, "low")
