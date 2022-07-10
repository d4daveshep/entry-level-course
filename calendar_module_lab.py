#  4.6.1.13 LAB: the calendar module
#  https://edube.org/learn/pe-2/lab-the-calendar-module-1
from calendar import Calendar

import pytest


class MyCalendar(Calendar):

    def count_weekday_in_year(self, year: int, weekday: int) -> int:
        """
        Counts the number of times the specified weekday occurs in the specified year

        Implementation:
        for each month in the year, iterate through the day, weekday tuple from Calendar.monthdays2calendar()
        if the day is > 0 and the weekday matches, then increment the count
        :param year:
        :param weekday:
        :return: the number of times the specified weekday occurs in the specified year
        """
        assert 0 < year
        assert 0 <= weekday <= 6

        count = 0

        for month in range(1, 13):
            for week in self.monthdays2calendar(year, month):
                for day, wkday in week:
                    if day > 0 and wkday == weekday:
                        count += 1

        return count


def test_count_weekday_in_year():
    cal = MyCalendar()

    try:
        assert cal.count_weekday_in_year(year=2019, weekday=12) == 52  # test invalid weekday
    except AssertionError:
        pass
    try:
        assert cal.count_weekday_in_year(year=2019, weekday=-12) == 52  # test invalid weekday
    except AssertionError:
        pass

    assert cal.count_weekday_in_year(year=2019, weekday=0) == 52
    assert cal.count_weekday_in_year(year=2000, weekday=6) == 53

