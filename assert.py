def read_int(prompt, min, max):

    i = input(prompt)
    i = int(i)
    assert (i > min and i < max)  # assert true, if false then AssertionError is raised
    return i

try:
    v = read_int("Enter a number from -10 to 10: ", -10, 10)
    print("The number is:", v)
except ValueError:
    print("Error: wrong input")
except AssertionError:
    print("Error: the value is not within permitted range (min..max)")
