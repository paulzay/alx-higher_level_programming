#!/usr/bin/python3
def search_replace(my_list, search, replace):
    clon = []
    for num in range(len(my_list)):
        if my_list[num] == search:
            clon.append(replace)
        else:
            clon.append(my_list[num])
    return clon
