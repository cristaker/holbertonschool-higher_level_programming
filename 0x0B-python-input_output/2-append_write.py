#!/usr/bin/python3
"""function appends a string"""


def append_write(filename="", text=""):
    """function"""

    with open(filename, 'a', encoding='UTF8') as f:
        data_write = f.write(text)
        return data_write
