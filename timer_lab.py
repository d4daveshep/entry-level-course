import pytest


def format_time_string(hrs: int, mins: int, secs: int) -> str:
    """
    Returns a formatted time string in format hh:mm:ss with leading zeros
    :param hrs:
    :param mins:
    :param secs:
    :return:
    """
    return (str(hrs)).zfill(2) + ":" + (str(mins)).zfill(2) + ":" + (str(secs)).zfill(2)


class Timer:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def __str__(self):
        return format_time_string(self.__hours, self.__minutes, self.__seconds)

    def next_second(self):
        self.__seconds += 1
        if self.__seconds // 60 > 0:
            self.__seconds %= 60
            self.__minutes += 1
        if self.__minutes // 60 > 0:
            self.__minutes %= 60
            self.__hours += 1
        if self.__hours // 24 > 0:
            self.__hours %= 24


    def prev_second(self):
        self.__seconds -= 1
        if self.__seconds < 0:
            self.__seconds = 59
            self.__minutes -= 1
        if self.__minutes < 0:
            self.__minutes = 59
            self.__hours -= 1
        if self.__hours < 0:
            self.__hours = 23

def test_timer():
    # test zero time
    timer = Timer()
    assert timer.__str__() == "00:00:00"

    # test max time
    timer = Timer(23, 59, 59)
    assert timer.__str__() == "23:59:59"

def test_next_second():
    # test inc second
    timer = Timer()
    timer.next_second()
    assert timer.__str__() == "00:00:01"

    # test inc second with rollover to next min
    timer = Timer(0, 0, 59)
    timer.next_second()
    assert timer.__str__() == "00:01:00"

    # test inc second with rollover to next hour
    timer = Timer(0,59,59)
    timer.next_second()
    assert timer.__str__() == "01:00:00"

    # test inc second at max time
    timer = Timer(23,59,59)
    timer.next_second()
    assert timer.__str__() == "00:00:00"

def test_prev_second():
    # test dec second
    timer = Timer(1,2,3)
    timer.prev_second()
    assert timer.__str__() == "01:02:02"

    # test dec second with roll-under minute
    timer = Timer(1,2,0)
    timer.prev_second()
    assert timer.__str__() == "01:01:59"

    # test dec second with roll-under hour
    timer = Timer(3,0,0)
    timer.prev_second()
    assert timer.__str__() == "02:59:59"

    # test dec second with roll-under max time
    timer = Timer(0,0,0)
    timer.prev_second()
    assert timer.__str__() == "23:59:59"

#
#
# print(timer)
# timer.next_second()
# print(timer)
# timer.prev_second()
# print(timer)
