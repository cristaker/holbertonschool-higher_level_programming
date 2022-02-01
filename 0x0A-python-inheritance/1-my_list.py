#!/usr/bin/python3


"""Class my_list"""


class MyList(list):
    """Class that inherits from list"""

    def print_sorted(self):
        """Method print sorted list"""

        l_sorted = self.copy()
        l_sorted.sort()

        print(l_sorted)
