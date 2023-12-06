#!/usr/bin/python3
def search_replace(my_list, search, replace):
    count = 0
    for i in my_list:
        count += 1
        if i == search:
            my_list[count - 1] = replace
    return my_list
