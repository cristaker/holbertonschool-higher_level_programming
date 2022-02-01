#!/usr/bin/python3


"""class base geometry"""


class BaseGeometry:
    """method down"""

    def area(self):
        """instance method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """instance method"""

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            raise ValueError("{} must be greater than 0".format(name))
