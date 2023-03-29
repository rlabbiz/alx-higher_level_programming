#!/usr/bin/python3
def search_replace(my_list, search, replace):
    lst = my_list[:]
    for i,  in lst:
        if lst[i] == search:
            lst[i] = replace
    return lst
lst = [1, 2, 3]
print(search_replace(lst, 2, 3))
