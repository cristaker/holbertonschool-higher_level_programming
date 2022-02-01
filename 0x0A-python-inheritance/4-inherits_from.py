#!/usr/bin/python3


"""Function"""


def inherits_from(obj, a_class):
    """method"""

    if isinstance(obj, a_class):
        return True
    elif type(obj) is a_class:
        return False
