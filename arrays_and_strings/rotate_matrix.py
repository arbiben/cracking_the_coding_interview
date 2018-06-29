# given an image representaed be an NxN matrix, 
# where each picel in the image is 4 bytes, 
# write a method to rotate the image by 90 degrees

n = 8;
matrix = [[x+y+10 for x in range(n)] for y in range(n)]

def print_matrix(matrix):
    print("--------------------------------")
    for i in range(len(matrix)):
        print(matrix[i])
    print("--------------------------------")

def rotate_matrix(matrix):
    last_elem = len(matrix[0])
    first_elem = -1
    for i in range(int(n/2)):
        last_elem -= 1
        first_elem += 1 
        for j in range(i, last_elem):
            temp = matrix[i][j]
            right_i = j
            right_j = last_elem
            bottom_i = last_elem
            bottom_j = last_elem - j
            left_i = last_elem - j
            left_j = first_elem
            
            matrix[i][j] = matrix[left_i][left_j]
            matrix[left_i][left_j] = matrix[bottom_i][bottom_j]
            matrix[bottom_i][bottom_j] = matrix[right_i][right_j]
            matrix[right_i][right_j] = temp

    return matrix

def rotate_matrix_with_data_structure(matrix):
    m = len(matrix[0])
    after_rotate = [[0 for x in range(m)] for y in range(m)]
    for i in range(m):
        for j in range(m):
            after_rotate[m-j-1][m-i-1] = matrix[i][j]


    return after_rotate
print("Before: ")
print_matrix(matrix)
print("\nAfter rotating no data structures O(n^2) speed O(1) space: ")
print_matrix(rotate_matrix(matrix))

print("\nAfter rotating with data structure O(n^2) speed and space: ")
print_matrix(rotate_matrix_with_data_structure(matrix))
