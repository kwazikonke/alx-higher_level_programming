#!/usr/bin/python3

""" Function that prints a texte with 2 lines after . ? and : """

def text_indentation(text):

    if type(text) is not str:
        raise TypeError("text must be a string")

    i=0
    for x in text:
        if i == 0:
            if x == ' ':
                continue
        else:
            i = 1
     if i == 1:
         if x == '?' or x == '.' or x == ':':
             print(x)
             print()
         else:
             print(a, end="")
