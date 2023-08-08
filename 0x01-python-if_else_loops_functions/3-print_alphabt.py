#!/usr/bin/python3
#3-print_alphabt.py
for x in range(97, 123):
    if (x != 101 and x != 113):
        print("{:s}".format(chr(x)), end="")

