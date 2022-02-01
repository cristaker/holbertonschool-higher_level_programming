#!/usr/bin/python3
"""function that writes a string"""


def write_file(filename="", text=""):
    """function"""

    with open(filename, 'w', encoding="UTF8") as f:
        return f.write(text)
