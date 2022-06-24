import math

import pytest

from point import Point


class Triangle:
    """
    Triangle is a composition of 3 Point objects.
    """

    def __init__(self, point1, point2, point3):
        self.__vertices = [point1, point2, point3]

    def perimeter(self):
        """
        perimeter is calculated using the Point.distance_from_point() method
        :return: length of the triangle sides
        """
        len_side1 = self.__vertices[0].distance_from_point(self.__vertices[1])
        len_side2 = self.__vertices[1].distance_from_point(self.__vertices[2])
        len_side3 = self.__vertices[0].distance_from_point(self.__vertices[2])
        return len_side1 + len_side2 + len_side3



def test_perimeter():
    triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))

    assert triangle.perimeter() == (1.0 + 1.0 + math.sqrt(2.0))
