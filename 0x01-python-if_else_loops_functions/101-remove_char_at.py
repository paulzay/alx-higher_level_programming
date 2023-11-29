#!/usr/bin/python3
def remove_char_at(str, n):
    chars = []

    for s in str:
        if str.index(s) != n:
            chars.append(s)
        else:
            continue

    return ''.join(chars)
