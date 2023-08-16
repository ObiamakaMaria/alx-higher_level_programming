#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []  # Initialize an empty list to store the new matrix
    
    for row in matrix:
        new_row = []  # This empty list  will store the new row
        for value in row:
            new_row.append(value ** 2)
        new_matrix.append(new_row)
    
    return new_matrix 
