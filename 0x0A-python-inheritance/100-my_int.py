#!/usr/bin/python3
"""inherits from int"""


class MyInt(int):
    """method down"""

    def __equal__(self, value):
        """instance equal"""

        return self.__true != value

    def __different__(self, value):
        """instance different"""

        return self.__true == value
