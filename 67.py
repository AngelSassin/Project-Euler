# the names
file = open('triangle.txt','r')
fileGrid = file.read().split('\n')
grid = []
for i in fileGrid:
    grid.append(i.split(' '))

# returns a grid where each node represents the maximum sum of the
#   possible paths from that node to the top.
def nodeSumPath():
    sumGrid = grid
    for i in range(0,len(grid)):
        for j in range(0,len(grid[i])):
            num = int(grid[i][j])
            if num == 0:
                break
            if i == 0:
                i = i
            elif j == 0:
                num += grid[i-1][j]
            elif i == j:
                num += grid[i-1][j-1]
            else:
                num += max(grid[i-1][j], grid[i-1][j-1])
            sumGrid[i][j] = num
    return sumGrid

# solves for the answer
sumGrid = nodeSumPath()
answer = max(sumGrid[len(sumGrid)-1])
print answer
