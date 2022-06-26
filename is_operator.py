class SampleClass:
    def __init__(self, val: object):
        self.val = val


obj1 = SampleClass(0)
obj2 = SampleClass(2)
obj3 = obj1
obj3.val += 1

print(obj1 is obj2)  # false
print(obj2 is obj3)  # false
print(obj3 is obj1)  # true
print(obj1.val, obj2.val, obj3.val)

string_1 = "Mary had a little "
string_2 = "Mary had a little lamb"
string_1 += "lamb"

print(string_1 == string_2)  # true because the strings are the same string
print(string_1 is string_2)  # false because they are different objects, but they happen to contain the same string
