import pytest


def digit_of_life(birthdate):
    date_chars = list(str(birthdate))
    date_digits = [int(d) for d in date_chars]
    date_sum = sum(date_digits)
    if date_sum > 9:
        date_sum = digit_of_life(date_sum)  # using recursion - how cool am I !!!
    return date_sum


def test_digit_of_life():
    assert digit_of_life(19991229) == 6
    assert digit_of_life(20000101) == 4
