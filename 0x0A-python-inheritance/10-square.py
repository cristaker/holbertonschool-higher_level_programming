#!/usr/bin/python3
"""class Sqquare inherits from rectangle"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """method down"""

    def __init__(self, size):
        """Instantiation initialized"""

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """Area instance"""

        return self.__size * self.__size
