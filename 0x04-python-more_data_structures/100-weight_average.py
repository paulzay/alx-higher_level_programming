#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    else:
        d = 0
        avg = 0

        for i in my_list:
            avg += i[0] * i[1]
            d += i[1]
        return float(avg / d)
