def mysum(*numbers):  # this is called the "splat" operator to take a variable number of args.  the args are presented as a tuple
    the_sum = 0
    for n in numbers:
        the_sum += n
    print(the_sum)

# def test_mysum():
mysum(1,2,3,4)

# mysum([1,2,3,4])  # this won't work as mysum function sees it as a tuple containing a list of numbers.

mysum(*[1,2,3,4])  # this works OK using the * preface to the list.  This expands the list into indificual digits