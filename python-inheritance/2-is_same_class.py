#!/usr/bin/python3

def is_same_class(obj, a_class):
    if isinstance(obj, a_class) and a_class != object:
        return True
    else:
        return False
