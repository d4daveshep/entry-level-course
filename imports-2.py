from math import pi, sin  # this imports just the pi and sin functions into my local namespace

print(pi)

print(sin(pi/2))

#print(math.e)  # but now i can't access other functions in the math namespace without specifically importing them
# gives a NameError - math not definded

# and we can still supersede the pi and sci functions with our own - Python doesn't complain
pi = 3.14

def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None


print(sin(pi / 2))
