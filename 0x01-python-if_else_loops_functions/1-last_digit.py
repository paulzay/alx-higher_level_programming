#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)


def last_digit(num):
    if num >= 0:
        return num % 10
    else:
        return (abs(num) % 10) * -1


last_number = last_digit(number)

if last_number > 5:
    print(f"Last digit of {number} is {last_number} and is greater than 5")
elif last_number == 0:
    print(f"Last digit of {number} is {last_number} and is 0")
elif last_number < 6 and last_number != 0:
    print(f"Last digit of {number} is {last_number} and\
is less than 6 and not 0")
