#!/usr/bin/python3


"""Matrix divided"""


def matrix_divided(matrix, div):
    """Matrix divide"""

    messagetype = "matrix must be a matrix (list of lists) of integers/floats"
    if not type(div) in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not matrix or not isinstance(matrix, list):
        raise TypeError(messagetype)

    lenel = 0
    messageesize = "Each row of the matrix must have the same size"

    for elements in matrix:
        if not elements or not isinstance(elements, list):
            raise TypeError(messagetype)
        if lenel != 0 and len(elements) != lenel:
            raise TypeError(messagesize)

        for number in elements:
            if not type(number) in (int, float):
                raise TypeError(messagetype)

    lenel = len(elements)

    m = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))

    return m
