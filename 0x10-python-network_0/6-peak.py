#!/usr/bin/python3
# find peak


def find_peak(list_of_integers):
    if len(list_of_integers) < 1:
        return None
    return max(list_of_integers)

if __name__ == "__main__":
    find_peak()
