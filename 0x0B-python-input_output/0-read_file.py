#!/usr/bin/python3
"""Read an file"""


def read_file(filename=""):
    """function"""

    with open(filename, 'r', encoding="utf8") as f:
        data = f.read()
        print(data, end='')
