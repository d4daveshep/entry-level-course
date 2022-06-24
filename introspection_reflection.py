class MyClass:
    pass


obj = MyClass()
obj.a = 1
obj.b = 2
obj.i = 3
obj.ireal = 3.5
obj.integer = 4
obj.z = 5


def incIntsI(obj):
    """
    Increment only the object properties that are ints starting with "i"
    :param any object:
    """
    for name in obj.__dict__.keys():  # iterate through through the object properties
        if name.startswith('i'):  # filter out the ones starting with "i"
            val = getattr(obj, name)  # get the value of the property
            if isinstance(val, int):  # if the value is an int
                setattr(obj, name, val + 1)  # then increment by 1 and save


print("Before", obj.__dict__)
incIntsI(obj)
print("After", obj.__dict__)
