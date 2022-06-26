class Fibonacci:
    def __init__(self, number_to_generate):
        # print("__init__")
        self.__number_to_generate = number_to_generate
        self.__counter = 0
        self.__previous_number_1 = self.__previous_number_2 = 1

    def __iter__(self):
        # print("__iter__")
        return self

    def __next__(self):
        # print("__next__")
        self.__counter += 1
        if self.__counter > self.__number_to_generate:
            raise StopIteration
        if self.__counter in [1, 2]:
            # the first two numbers in the sequence are 1 so if we're only asked to generate the first 1 or 2 number
            # then result will be 1
            return 1
        return_value = self.__previous_number_1 + self.__previous_number_2
        self.__previous_number_1, self.__previous_number_2 = self.__previous_number_2, return_value  # cool way to reassign two values at once
        return return_value


for i in Fibonacci(10):
    print(i, end=", ")
