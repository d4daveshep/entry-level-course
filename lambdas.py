# Lambdas are an alternative way to declaire a function, the main benefits being brevity and using
# as anonymous functions

two = lambda: 2  # this function is assigned to the name "two" and just return the number 2
sqr = lambda x: x * x  # returns the square of x,  assigned to the name "sqr"
pwr = lambda x, y: x ** y  # return x raised to the power y, assigned to the name "pwr"

# use them like normal functions
assert two() == 2
try:
    assert two(3) == 2  # TypeError - no arg constructor only
except TypeError:
    assert True

assert sqr(3) == 9
assert pwr(2,4) == 16

# for a in range(-2, 3):
#     print(sqr(a), end=" ")
#     print(pwr(a, two()))


def print_function(args, func):
    for x in args:
        print('f(', x,')=', func(x), sep='')


def poly(x):
    return 2 * x**2 - 4 * x + 2


print_function([x for x in range(-2, 3)], poly)  # using the above defined function poly(x)

print_function([x for x in range(-2,3)], lambda x: 2 * x**2 - 4 * x + 2)  # now using an anonymous lambda
