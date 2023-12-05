#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    nums_list = []

    if not my_list:
        return None
    else:
        for num in my_list:
            if num % 2 == 0:
                nums_list.append(num)
            else:
                nums_list.append(False)
        return nums_list
