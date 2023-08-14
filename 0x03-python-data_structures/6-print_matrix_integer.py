#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if type(matrix)== list:
        for i in range(len(matrix)):
            for x in range(len(matrix[i])):
                print("{:d}{}".format(matrix[i][j],'' if x == len(matrix[i])-1 else ''), end="")
                print ("")
