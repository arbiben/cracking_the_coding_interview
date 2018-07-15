# implement the functions that one might see on many image editing programs.
# That is, given a screen, a point and a new color, fill in the surrounding are
# until the color changes from the original color

def fill_color(matrix, i, j, new_color):
    curr_color = matrix[i][j]
    fill_color_helper(matrix, i, j, curr_color, new_color)

def fill_color_helper(matrix, i, j, curr, new):
    if is_out_of_bounds(matrix, i, j) or matrix[i][j] != curr:
        return

    matrix[i][j] = new
    fill_color_helper(matrix, i+1, j, curr, new)
    fill_color_helper(matrix, i-1, j, curr, new)
    fill_color_helper(matrix, i, j+1, curr, new)
    fill_color_helper(matrix, i, j-1, curr, new)

def is_out_of_bounds(matrix, i, j):
    if i < 0 or i > len(matrix)-1:
        return True
    if j < 0 or j > len(matrix[0])-1:
        return True
    return False

# test::
h, w = 5, 7
matrix = [[x for x in range(w)] for y in range(h)]
matrix[2] = [3 for _ in range(w)]
fill_color(matrix, 2, 3, 0)
for l in range(len(matrix)):
    print(matrix[l])
