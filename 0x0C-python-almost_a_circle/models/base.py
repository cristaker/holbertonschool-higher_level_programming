#!/usr/bin/python3
"""class base"""


class base:
    """attribuites"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initializes instance"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
