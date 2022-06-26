# this is an example of a generator (aka iterator)
# it implements the iterator protocol (not an interface or subclass)
def fibonacci(number_to_generate):
    previous_number_1 = previous_number_2 = 1
    for i in range(number_to_generate):
        if i in [0, 1]:
            yield 1
        else:
            return_number = previous_number_1 + previous_number_2
            previous_number_2, previous_number_1 = previous_number_1, return_number
            yield return_number


class IteratorIncluded:
    # a class that is composed of an iterator
    def __init__(self, n):
        self.__iterator = fibonacci(n)

    def __iter__(self):
        return self.__iterator


fibs = list(fibonacci(10))
print(fibs)

fib = IteratorIncluded(10)
for i in fib:
    print(i, end=", ")
