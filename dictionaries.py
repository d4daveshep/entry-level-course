# How to merge two dictionaries
# in Python 3.5+

x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}

z = {**x, **y}

print(f"dictionary 1 is {x}")
print(f"dictionary 2 is {y}")

print(f"merged dictionary is {z}")
print("NOTE that value for key=\'b\' is overwritten")