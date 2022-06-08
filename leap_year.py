# What is a leap year?
# To be a leap year, the year number must be divisible by four – except for end-of-century years, which must be divisible by 400.
# This means that the year 2000 was a leap year, although 1900 was not. 2020, 2024 and 2028 are all leap years.
import pytest

def is_leap_year(year):
    if(year % 400 == 0):
        return True
    if(year % 100 == 0):
        return False
    if(year % 4 == 0):
        return True
    else:
        return False

def test_is_leap_year():
    assert(is_leap_year(2000) == True)  # 2000 is a leap year
    assert(is_leap_year(2004) == True)  # 2004 is a leap year
    assert(is_leap_year(1999) == False)  # 1999 is not a leap year
    assert(is_leap_year(1900) == False)  # 1900 is not a leap year


