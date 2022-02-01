#!/usr/bin/python3
"""Class define square inherits from rectangle"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Method down"""

    def __init__(self, size):
        """instantiation initialized"""

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """area instance"""

        return self.__size * self.__size

    def __str__(self):
        """self instance"""

        return "[Square] {}/{}".format(self.__size, self.__size)
