from random import random, seed, randint, choice, sample  # this is the random()

def print_randoms():
    for i in range(3):
        print(random())  # random number between 0 and 1

seed()  # seeds with current timestamp
print_randoms()
print()
seed(0) # sets the seed - so will give same random sequence
print_randoms()

# randint prduces random ints between beg and end
for i in range(10):
    print(randint(1,10),end=" ")

print()
my_list = [i+1 for i in range(10)]  # create a list from 1 to 10
print(my_list)
print(choice(my_list))  # pick a number from my list
print(sample(my_list, 5))  # pick 5 from my list
print(sample(my_list,10))  # pick all from my list - randomise the list



