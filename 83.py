# the matrix
file = open('matrix.txt','r')
rows = file.read().split('\n')
matrix = []
for r in rows:
    matrix.append(r.split(','))
matrix.remove([''])

# returns the minimum sum matrix from the matrix in the file
def getMatrixSum():
    sumMatrix = [[None]*len(matrix)]*len(matrix[0])    
    for j in range(0,len(matrix[0])):
        for i in range(0,len(matrix)):
            if j == 0:
                row = sumMatrix[i][:]
                row[j] = int(matrix[i][j])
                sumMatrix[i] = row
            else:
                row = sumMatrix[i][:]
                row[j] = int(matrix[i][j])+sumMatrix[i][j-1]
                sumMatrix[i] = row
    changed = True
    while changed:
        previous = sumMatrix[:]
        changed = False
        for j in range(0,len(matrix[0])):
            for i in range(0,len(matrix)):
                if j == 0 and i == 0:
                    row = sumMatrix[i][:]
                    row[j] = int(matrix[i][j])
                    sumMatrix[i] = row
                elif j == 0 and i == len(matrix)-1:
                    row = sumMatrix[i][:]
                    row[j] = int(matrix[i][j]) + min(previous[i][j+1],previous[i-1][j])
                    sumMatrix[i] = row
                elif j == len(matrix[0])-1 and i == 0:
                    row = sumMatrix[i][:]
                    row[j] = int(matrix[i][j]) + min(previous[i][j-1],previous[i+1][j])
                    sumMatrix[i] = row
                elif j == len(matrix[0])-1 and i == len(matrix)-1:
                    row = sumMatrix[i][:]
                    row[j] = int(matrix[i][j]) + min(previous[i][j-1],previous[i-1][j])
                    sumMatrix[i] = row
                elif i == len(matrix)-1:
                    row = sumMatrix[i][:]
                    row[j] = int(matrix[i][j]) + min(previous[i][j-1],previous[i-1][j],previous[i][j+1])
                    sumMatrix[i] = row
                elif i == 0:
                    row = sumMatrix[i][:]
                    row[j] = int(matrix[i][j]) + min(previous[i][j-1],previous[i+1][j],previous[i][j+1])
                    sumMatrix[i] = row
                elif j == len(matrix[0])-1:
                    row = sumMatrix[i][:]
                    row[j] = int(matrix[i][j]) + min(previous[i][j-1],previous[i-1][j],previous[i+1][j])
                    sumMatrix[i] = row
                elif j == 0:
                    row = sumMatrix[i][:]
                    row[j] = int(matrix[i][j]) + min(previous[i-1][j],previous[i+1][j],previous[i][j+1])
                    sumMatrix[i] = row
                else:
                    row = sumMatrix[i][:]
                    row[j] = int(matrix[i][j]) + min(previous[i][j-1],previous[i+1][j],previous[i][j+1],previous[i-1][j])
                    sumMatrix[i] = row
                if previous != None and sumMatrix[i][j] != previous[i][j]:
                    changed = True
    return sumMatrix

# solves for answer
answer = getMatrixSum()
print answer[len(theSumMatrix)-1][len(theSumMatrix[0])-1]
