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
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[0])):
            if i == 0 and j == 0:
                row = sumMatrix[i][:]
                row[j] = int(matrix[i][j])
                sumMatrix[i] = row
            elif i == 0:
                row = sumMatrix[i][:]
                row[j] = int(matrix[i][j]) + sumMatrix[i][j-1]
                sumMatrix[i] = row
            elif j == 0:
                row = sumMatrix[i][:]
                row[j] = int(matrix[i][j]) + sumMatrix[i-1][j]
                sumMatrix[i] = row
            else:
                row = sumMatrix[i][:]
                row[j] = int(matrix[i][j]) + min(sumMatrix[i][j-1],sumMatrix[i-1][j])
                sumMatrix[i] = row
    return sumMatrix

# solves for answer
answer = getMatrixSum()
print answer[len(answer)-1][len(answer[0])-1]
