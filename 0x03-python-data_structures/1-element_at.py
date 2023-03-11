#!/usr/bin/python3

""" function retrieves an element from a list that given as second argument """
def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return None
    else:
        return my_list.index(idx)
