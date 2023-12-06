#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    nums = []

    for num in my_list:
        if num in nums:
            continue
        else:
            nums.append(num)

    for i in nums:
        total += i

    return total
