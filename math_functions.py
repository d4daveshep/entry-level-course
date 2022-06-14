from math import ceil, floor, trunc

x = 1.4
y = 2.6

print(floor(x), floor(y))  # floor moves the number to next left int on the number line
print(floor(-x), floor(-y))

print(ceil(x), ceil(y))  # ceil moves the number to next right int on the number line
print(ceil(-x), ceil(-y))

print(trunc(x), trunc(y))  # trunc moves the number to the next int closes ot zero on number line
print(trunc(-x), trunc(-y))
