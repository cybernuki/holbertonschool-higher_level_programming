#!/usr/bin/python3
def print_last_digit(number):
    last_digit = 0
    if number < 0:
        last_digit = (abs(number) % 10) * -1
    else:
        last_digit = number % 10
    print(last_digit, end="")
    return last_digit
