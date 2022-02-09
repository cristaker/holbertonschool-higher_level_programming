#!/usr/bin/python3
"""class inherits from base"""
from models.base import Base


class Rectangle(Base):
    """class inherits from base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """instance"""
        
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
