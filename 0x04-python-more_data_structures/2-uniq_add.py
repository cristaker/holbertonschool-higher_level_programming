#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = set(my_list)
    addnum = 0

    for i in uniq:
        addnum += i
    return (addnum)
