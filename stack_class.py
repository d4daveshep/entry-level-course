class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val


class CountingStack(Stack):
    def __init__(self):
        Stack.__init__(self)  # call the superclass constructor
        self.__counter = 0  # private subclass attribute

    def get_counter(self):
        return self.__counter

    def pop(self):  # override the pop method
        self.__counter += 1
        return Stack.pop(self)  # call the superclass method


stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter())
