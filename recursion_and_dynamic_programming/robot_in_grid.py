# a robot is sitting on the top left corner of a 2d array.
# the robot can move right and down, some indices are "off limits"
# design an algorithm to find a path to the bottom right
count = 0

def plan_path(matrix, i, j):
    global count
    w = len(matrix[0])-1
    h = len(matrix)-1
    if i>h or j>w:
        return False

    if i==h and j==w:
        return ("I'm Home!!")

    if matrix[i][j] == -1:
        return False

    count+= 1
    return plan_path(matrix, i, j+1) or plan_path(matrix, i+1, j)

# dynamic
def plan_path_dy(matrix, i, j):
    global count
    w = len(matrix[0])-1
    h = len(matrix)-1

    if i>h or j>w:
        return False

    if matrix[i][j] == -2:
        return False

    if matrix[i][j] == -1:
        return False

    if i==h and j==w:
        return ("I'm Home!!")

    matrix[i][j] = -2
    count += 1
    return plan_path_dy(matrix, i, j+1) or plan_path_dy(matrix, i+1, j)



w, h = 8, 5
matrix = [[0 for x in range(w)] for y in range(h)]
matrix[0][3] = -1
matrix[1][3] = -1
matrix[2][3] = -1
matrix[2][1] = -1
matrix[2][2] = -1



print(plan_path(matrix, 0,0))
print("{} steps without dynamic programming".format(count))
count = 0
print(plan_path_dy(matrix, 0,0))
print("{} steps with dynamic programming".format(count))
