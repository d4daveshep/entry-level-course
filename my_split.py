# Exercise 3.2.1.18
import pytest


def mysplit(strng):
    lst = []

    strng = strng.strip()
    if len(strng) == 0:
        return lst

    while True:
        i = strng.find(" ")
        if i == -1:
            lst.append(strng)
            return lst
        lst.append(strng[:i])
        strng = strng[i + 1:]


# print(mysplit("To be or not to be, that is the question"))
# print(mysplit("To be or not to be,that is the question"))
# print(mysplit("   "))
# print(mysplit(" abc "))
# print(mysplit(""))

# expected output
# ['To', 'be', 'or', 'not', 'to', 'be,', 'that', 'is', 'the', 'question']
# ['To', 'be', 'or', 'not', 'to', 'be,that', 'is', 'the', 'question']
# []
# ['abc']
# []
def test_mysplit():
    assert [] == mysplit("")

    split = ['To', 'be', 'or', 'not', 'to', 'be,', 'that', 'is', 'the', 'question']
    assert split == mysplit("To be or not to be, that is the question")

    split = ['To', 'be', 'or', 'not', 'to', 'be,that', 'is', 'the', 'question']
    assert split == mysplit("To be or not to be,that is the question")

    assert [] == mysplit("   ")
    assert ["abc"] == mysplit(" abc ")
