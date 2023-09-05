#!/usr/bin/python3

"""
Function that prints a square with the character #

"""

def print_square(size):
    if type(size) is not int or \ (type(size) is not float and size < 0):
        raise TypeError("size must be an integer")
    if not (size >=0):
        raise ValueError("size must be >=0")

    for i in range(size):
                         for j in range(size):
                          print("#", end="")
                         print()
