#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    lst = my_list[:]
    for index, i in enumerate(my_list):
        if i % 2 == 0:
            lst[index] = True
        else:
            lst[index] = False
    return lst
