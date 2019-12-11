#!/bin/bash/python3
def remove_char_at(str, n):
    str_new = ""
    for i in range(len(str)):
        if i != n:
            str_new += str[i]
    return str_new
