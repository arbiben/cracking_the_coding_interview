# a robot is sitting on the top left corner of a 2d array.
# the robot can move right and down, some indices are "off limits"
# design an algorithm to find a path to the bottom right

def plan_path(matrix, i, j):
    w = len(matrix[0])-1
    h = len(matrix)-1
    print("{},{}".format(i, j))
    if i>h or j>w:
        print("out of range!")
        return False

    if i==h and j==w:
        return ("I'm Home!!")

    if matrix[i][j] == -1:
        print("BLOCK at {},{}".format(i, j))
        return False

    return plan_path(matrix, i, j+1) or plan_path(matrix, i+1, j)



w, h = 8, 5
matrix = [[0 for x in range(w)] for y in range(h)]
matrix[0][2] = -1
matrix[2][1] = -1
matrix[1][5] = -1
matrix[2][5] = -1
matrix[3][7] = -1
print(plan_path(matrix, 0,0))
