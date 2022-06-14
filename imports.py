import math  # imports the math library, this also allows us to use the math namespace


def sin(x):  # I dcan define a function that doesn't override the math namesapce - this could be confusing though
    if 2 * x == pi:
        return 0.99999999
    else:
        return None


pi = 3.14  # same with local constants, these can have same name an other namespaces

print(sin(pi/2))  # using local namespace
print(math.sin(math.pi/2))  # using math namespace


