# returns the sum of the diagonals of the square spiral made from the
#   specified number. PRECONDITION: num is odd
def sumDiagonalsSpiral(num):
    iterations = (num-1)/2
    diagonals = [1]
    for i in range(0,iterations):
        difference = (i+1)*2
        for j in range(0,4):
            diagonals.append(diagonals[len(diagonals)-1]+difference)
    return sum(diagonals)

# solves for the answer.
answer = sumDiagonalsSpiral(1001)
print answer
