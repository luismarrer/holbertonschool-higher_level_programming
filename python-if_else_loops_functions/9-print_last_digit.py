#!/usr/bin/python3
def print_last_digit(number):
    last_number = str(number)[-1]
    if "9" >= last_number >= "0":
        print("{}" .format(last_number), end="")
        return last_number
    else:
        print("Traceback (most recent call last):")
