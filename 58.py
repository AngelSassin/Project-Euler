import math

# returns True if the specified number is prime
def isPrime(a):
    if a <= 1:
        return False
    for i in range(2,int(math.floor(math.sqrt(a)))+1):
        if a%i == 0:
            return False
    return True

# returns the side length of the spiral square whose ratio of the number
#   of prime diagonals to the number of diagonals is less than r.
def getSpiralSqrWithLessRatio(r):
    diagonals = [1]
    numPrimes = 0
    iteration = 1
    while numPrimes*1.0/len(diagonals) >= r or len(diagonals) == 1:
        for x in range(0,3):
            diagonals.append(diagonals[len(diagonals)-1]+(1+iteration))
            if isPrime(diagonals[len(diagonals)-1]):
                numPrimes += 1
        diagonals.append(diagonals[len(diagonals)-1]+(1+iteration))
        iteration += 2
    return iteration

# solves for the answer
answer = getSpiralSqrWithLessRatio(10/100.0)
print answer
