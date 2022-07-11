# Exercise 1.5 from Python Workout book
# Write a function to convert from hex to decimal (digit by digit)

import pytest

HEX_DIGITS = "0123456789abcdef"


def convert_hex_to_decimal_int(hex_string):
    dec = 0

    if not hex_string:
        raise ValueError(f"{hex_string} is not a valid hex number")

    for ch in hex_string:
        if ch not in HEX_DIGITS:
            raise ValueError(f"{hex_string} is not a valid hex number")

    for pos, digit in enumerate(reversed(hex_string)):
        # set through the hex string in reverse order
        # enumerate() gives us the position of the digit

        dec += HEX_DIGITS.index(digit) * (16 ** pos)
        # look up the digit in the HEX_DIGITS multiply by 16^position in hex_string

    return dec


def test():
    try:
        convert_hex_to_decimal_int("")  # empty string is not valid
        assert False
    except ValueError:
        assert True

    try:
        convert_hex_to_decimal_int("12345qwerty")  # non hex characters is not valid
        assert False
    except ValueError:
        assert True

    try:
        convert_hex_to_decimal_int(1231)
        assert False
    except TypeError:
        assert True

    assert convert_hex_to_decimal_int("0") == 0
    assert convert_hex_to_decimal_int("3") == 3
    assert convert_hex_to_decimal_int("a") == 10
    assert convert_hex_to_decimal_int("f") == 15

    assert convert_hex_to_decimal_int("10") == 16
    assert convert_hex_to_decimal_int("50") == 80
