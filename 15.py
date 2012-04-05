import math

# returns the number of paths to the specified node
def getNodeSum(row,col):
    grid = []
    for i in range(0,col+1):
        grid.append([])
        for j in range(0,row+1):
            grid[i].append([])
    for i in range(0,row+1):
        for j in range(0,col+1):
            if i == 0 or j == 0:
                grid[i][j] = 1
            else:
                grid[i][j] = grid[i-1][j] + grid[i][j-1]
    return grid[row][col]

# solves for the answer
answer = getNodeSum(20,20)
print answer
