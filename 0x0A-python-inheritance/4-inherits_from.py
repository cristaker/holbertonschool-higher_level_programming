#!/usr/bin/python3


"""Function"""


def inherits_from(obj, a_class):
    """method"""

    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
