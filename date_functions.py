import pytest


def is_year_leap(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    else:
        return False


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if month == 2 and is_year_leap(year):
        return 29
    else:
        return month_days[month - 1]


#
# Write your new code here.
#
def day_of_year(year, month, day):
    total_days = day
    for m in range(1, month):
        total_days += days_in_month(year, m)
    return total_days


def test_functions():
    assert (365 == day_of_year(2022, 12, 31))
    assert (60 == day_of_year(1999, 3, 1))
