#!/usr/bin/python3
"""Define a class rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Methos down"""

    def __init__(self, width, height):
        """initialize instance"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
