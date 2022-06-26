# this behaves exactly like the range function
def func(n):
    for i in range(n):
        yield i

# use the above function as an generator
for v in func(5):
    print(v)

# here's another generator that provides powers of 2
def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2

for v in powers_of_2(8):
    print(v)

# generators can be used in a list comprehension
t = [x for x in powers_of_2(5)]
print(t)

t = (x for x in powers_of_2(5))
for i in t:
    print(i)



