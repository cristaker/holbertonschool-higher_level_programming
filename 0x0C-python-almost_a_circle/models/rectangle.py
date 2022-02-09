#!/usr/bin/python3
"""class inherits from base"""
from models.base import Base


class Rectangle(Base):
    """class inherits from base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """instance"""
        
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
