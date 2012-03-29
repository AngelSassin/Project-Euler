# returns the sum of the squares of the first 100 natural numbers.
def getSumOfSquares():
    x = []
    for i in range(0,100):
        x.append(i+1)
    sum = 0
    for i in x:
        sum += i**2
    return sum

# returns the square of the sums of the first 100 natural numbers.
def getSquareOfSums():
    x = []
    for i in range(0,100):
        x.append(i+1)
    sum = 0
    for i in x:
        sum += i
    square = sum**2
    return square

# solve for the answer
answer = getSquareOfSums() - getSumOfSquares()
print answer
