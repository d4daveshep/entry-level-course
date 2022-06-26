class SuperOne:
    var_a = 10
    def func_a(self):
        return 11


class SuperTwo:
    var_b = 20
    def func_b(self):
        return 21


class Sub(SuperOne, SuperTwo): # multiple inheritance
    pass


def printBases(cls: object) -> object:
    print("(", end="")
    for x in cls.__bases__:
        print(x.__name__, end=" ")
    print(")")


printBases(SuperOne)
printBases(SuperTwo)
printBases(Sub)

obj = Sub()
print(obj.var_a, obj.func_a())
print(obj.var_b, obj.func_b())
