#!/usr/bin/python3

""" Function that divides all elements of a matrix
    matrix must be in a list of lists of integers or floats
    raise a TypeError exception with a specific msg
"""
def matrix_divided(matrix, div):
  if not isinstance(matrix, list) or not all(isinstance(row,list) for row in matrix) \
          or not all(isinstance(num, (int,float)) for row in matrix for num in row):
    raise TypeError("matrix must be a matrix (list of lists) of integers/float")

""" Checking if all rows have the same size """
if len(set(len(row) for row in matrix)) !=1:
    raise TypeError("Each row of the matrix must have the same size")

if not isinstance(div, (int,float)):
    raise TypeError("div must be a number")

if div == 0;
  raise ZeroDivisionError("division by zero")

  result_matrix = [[round(num / div, 2) for num in row] for row in matrix]

  return result_matrix
