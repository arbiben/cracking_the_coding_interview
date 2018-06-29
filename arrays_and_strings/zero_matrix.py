# given an array of NxM, for every location where the val is 0
# the etire row and column are set to 0
import random
n = 3
m = 4

test_matrix = [[random.randint(0,10) for _ in range(m)] for _ in range(n)]

def print_matrix(matrix_for_print):
    print("----------------------------------------")
    for i in range(len(matrix_for_print)):
        print(matrix_for_print[i])
    print("----------------------------------------")

def zero_line_and_row(matrix_temp, i, j):
    for k in range(len(matrix_temp[i])):
        matrix_temp[i][k] = 0

    for k in range(len(matrix_temp)):
        matrix_temp[k][j] = 0

    return matrix_temp

def zero_matrix(matrix):
    matrix_copy = [row[:] for row in matrix] 

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                matrix_copy = zero_line_and_row(matrix_copy, i, j)

    return matrix_copy

def null_row(matrix_r, row):
    for i in range(len(matrix_r[row])):
        matrix_r[row][i] = 0
    
    return matrix_r

def null_column(matrix_c, column):
    for i in range(len(matrix_c)):
        matrix_c[i][column] = 0
    
    return matrix_c

def zero_matrix_clean(matrix):
    rows = [False] * len(matrix)
    column = [False] * len(matrix[0])
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                rows[i] = True
                column[j] = True

    for i in range(len(rows)):
        if rows[i]:
            matrix = null_row(matrix, i)

    for i in range(len(column)):
        if column[i]:
            matrix = null_column(matrix, i)

    return matrix

print("before with extra 2d array")
print_matrix(test_matrix)

print("after with extra 2d array (O(n^2) space)")
print_matrix(zero_matrix(test_matrix))

print("after with no extra array (O(n) space)")
print_matrix(zero_matrix_clean(test_matrix))
