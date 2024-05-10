#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv

    if len(argv) == 2:
        str = "argument"
    else:
        str = "arguments"
    if len(argv) == 1:
        str += "."
    else:
        str += ":"
    print("{} {}" .format(len(argv) - 1, str))
    for i in range(1, len(argv)):
        print("{}: {}" .format(i, argv[i]))
