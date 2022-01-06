#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return (0)
    else:
        average = 0
        value = 0
    for i in my_list:
        value += (i[0] * i[1])
        average += (i[1])
    return (value / average)
