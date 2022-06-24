import math

import pytest


class Point:

    def __init__(self, x=0.0, y=0.0):
        self.__x = float(x)
        self.__y = float(y)

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        return math.hypot(x - self.getx(), y - self.gety())

    def distance_from_point(self, point):
        return self.distance_from_xy(point.getx(), point.gety())


def test_constructor():
    point = Point()
    assert point.getx() == 0.0
    assert point.gety() == 0.0

    point = Point(1.1, 2.2)
    assert point.getx() == 1.1
    assert point.gety() == 2.2


def test_distance_from_coords():
    point1 = Point(0, 0)
    point2 = Point(1, 1)
    assert point1.distance_from_xy(1, 1) == math.sqrt(2.0)
    assert point2.distance_from_xy(0, 0) == math.sqrt(2.0)


def test_distance_from_point():
    point1 = Point(0, 0)
    point2 = Point(1, 1)
    assert point1.distance_from_point(point2) == math.sqrt(2.0)
    assert point2.distance_from_point(point1) == math.sqrt(2.0)
