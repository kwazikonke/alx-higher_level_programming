#!/usr/bin/python3
"""
Function that add two integers
raise a TypeError exception,
and return addition of a and b
"""
def add_integer(a,b=98):
    if type(a) not in [int,float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int,float]:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a+b
