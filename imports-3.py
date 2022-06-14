from math import *  # imports everything from the math module - DON'T DO THIS - IT'S LAZY AND CREATES NAMESPACE CLASHES

import math as my_math  # this uses an alias and could be used to avoid namespace clashes

print(pi)
print(my_math.pi)
# print(math.pi)  # math namespace not imported

from math import pi as my_pi  # and we can just import one function and give it an alias
print(my_pi)
