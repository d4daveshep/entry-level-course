import pytest


class WeekDayError(Exception):
    pass


class Weeker:
    days = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")

    def __init__(self, day):
        if day in Weeker.days:
            self.__day = day
        else:
            raise WeekDayError

    def __str__(self):
        return self.__day

    def add_days(self, n):
        assert n >= 0

        idx = Weeker.days.index(self.__day)  # find index of curent day
        idx += n
        idx %= 7  # index of new date
        self.__day = Weeker.days[idx]  # set new day
        return self.__day

    def subtract_days(self, n):
        assert n >= 0

        idx = Weeker.days.index(self.__day)  # find index of curent day
        idx -= n
        idx %= 7  # index of new date
        self.__day = Weeker.days[idx]  # set new day
        return self.__day


# try out pytest.fixture for lols
@pytest.fixture
def days():
    return ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")


def test_constructor(days):  # use fixture above cos i can
    for day in days:
        try:
            weeker = Weeker(day)
            assert weeker.__str__() == day
        except:
            assert False

    try:
        weeker = Weeker("Monday")
        assert False
    except WeekDayError:
        pass


def test_add_days():
    weeker = Weeker("Mon")
    day15 = weeker.add_days(15)
    assert day15 == "Tue"

    try:
        weeker.add_days(-5)
        assert False
    except AssertionError:
        pass

def test_subtract_days():
    weeker = Weeker("Tue")
    day23 = weeker.subtract_days(23)
    assert day23 == "Sun"

    try:
        weeker.subtract_days(-5)
        assert False
    except AssertionError:
        pass
    except:
        assert False
