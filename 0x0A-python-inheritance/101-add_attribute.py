#!/usr/bin/python3


"""Function add attributes to object"""


def add_attribute(obj, name, value):
    """new attribute"""

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
