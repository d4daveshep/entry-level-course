# filter(function, iterable)

# The filter() function returns an iterator were the items are filtered through a function
# to test if the item is accepted or not.

# function is just like when using map().  Lambdas are a good option here.

ages = [5, 12, 17, 18, 24, 32]

def over18(x):  # return True if 18 or over
  if x < 18:
    return False
  else:
    return True

adults = filter(over18, ages)  # returns only those from ages that are

adults = filter(lambda x: x >= 18, ages)  # same thing using a lambda - avoids defining a separate function

for x in adults:
  print(x)


#  here's another example
from random import seed, randint

seed()
data = [randint(-10,10) for x in range(5)]
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))  # filter out the positive even numbers

print(data)
print(filtered)