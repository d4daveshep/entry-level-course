# In 1937, a German mathematician named Lothar Collatz formulated an intriguing hypothesis (it still remains unproven)
# which can be described in the following way:
#
#     take any non-negative and non-zero integer number and name it c0;
#     if it's even, evaluate a new c0 as c0 ÷ 2;
#     otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1;
#     if c0 ≠ 1, skip to point 2.
#
# The hypothesis says that regardless of the initial value of c0, it will always go to 1.

import pytest

def collatz(c0):
    steps = 0
    while c0 != 1:
        steps += 1
        if c0 % 2 == 0:
            c0 /= 2
        else:
            c0 = 3 * c0 + 1

    return steps



def test_collatz():
    assert(17 == collatz(15))
    assert (4 == collatz(16))
    assert (62 == collatz(1023))

