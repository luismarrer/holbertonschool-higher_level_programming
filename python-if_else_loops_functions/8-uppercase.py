#!/usr/bin/python3
def uppercase(str):
    for index in str:
        if ord("z") >= ord(index) >= ord("a"):
            char = ord(index) - 32
        else:
            char = ord(index)
        print("{}" .format(chr(char)), end="")
    print("")
