# the initial triangle grid.
grid = [[75],[95,64],[17,47,82],[18,35,87,10],[20,4,82,47,65],[19,1,23,75,3,34],[88,2,77,73,7,63,67],[99,65,4,28,6,16,70,92],[41,41,26,56,83,40,80,70,33],[41,48,72,33,47,32,37,16,94,29],[53,71,44,65,25,43,91,52,97,51,14],[70,11,33,28,77,73,17,78,39,68,17,57],[91,71,52,38,17,14,91,43,58,50,27,29,48],[63,66,4,68,89,53,67,30,73,16,69,87,40,31],[04,62,98,27,23,9,70,98,73,93,38,53,60,4,23]]

# returns a grid where each node represents the maximum sum of the
#   possible paths from that node to the top.
def nodeSumPath():
    sumGrid = grid
    for i in range(0,len(grid)):
        for j in range(0,len(grid[i])):
            num = grid[i][j]
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


