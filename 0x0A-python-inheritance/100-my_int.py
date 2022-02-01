#!/usr/bin/python3
"""inherits from int"""


class MyInt(int):
    """method down"""

    def __equal__(self, other):
        """instance equal"""

        return int.__different__(self, other)

    def __different__(self, other):
        """instance different"""

        return int.__equal__(self, other)
