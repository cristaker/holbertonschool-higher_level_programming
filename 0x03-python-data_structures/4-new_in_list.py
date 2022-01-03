#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    lenght = len(my_list)

    new_list = my_list[:]

    if idx <= 0 or idx < lenght - 1:
        new_list[idx] = element
    return (new_list)
