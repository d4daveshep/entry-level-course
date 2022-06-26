# map(function, list)
#
# The map() function executes a specified function for each item in an iterable.
# The item is sent to the function as a parameter.

# The map() function applies the function passed by its first argument to all its second argument's elements,
# and returns an iterator delivering all subsequent function results.

# Map() returns a generator / iterable

# Anonymous lambda functions are a good way to define the function

list_1 = [x for x in range(5)]
print(list_1)
list_2 = list(map(lambda x: 2 ** x, list_1))  # calculate 2^X for all items in list_1 and return them in a list
print(list_2)

for x in map(lambda x: x * x, list_2):
    print(x, end=' ')
print()

