#!/usr/bin/python3
"""Define a Rectangle class"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """method down"""

    def __init__(self, width, height):
        """Instatiation initialized"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Area methodd"""

        return self.__width * self.__height

    def __str__(self):
        """str method"""

        return "[Rectangle] {}/{}".format(self.__width, self.__height)
