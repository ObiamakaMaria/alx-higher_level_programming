#!/usr/bin/python3

square_matrix_map = lambda matrix: list(map(lambda row: list(map(lambda a: a * a, row)), matrix))

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_map(matrix)
print(new_matrix)
print(matrix)
