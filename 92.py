# When continuously finding the sum of the square of the digits of a number, the
# chain eventually reaches either 1 or 89, whose chains themselves do the same.

# How many starting numbers below ten million arrive at 89?

# NOTE: The sum of the squares of the digits in any integer below ten million
# is never greater than 567.

# NOTE 2: To get to a sum of 89, you need 25 and 64 or 9, 16, and 64

def sumSquareDigits(n):
    total = 0
    while n:
        total += (n%10)**2
        n /= 10
    return total

sumNums = [0]*568
sumNums[1] = 1
sumNums[89] = 89
totalTo89 = 1

def endChain(n):
    sSquare = sumSquareDigits(n)
    seen = [n]
    while sumNums[sSquare] == 0:
        seen.append(sSquare)  
        sSquare = sumSquareDigits(sSquare)
    for x in seen:
        sumNums[x] = sumNums[sSquare]
    if sumNums[sSquare] == 89:
        return len(seen)
    return 0

# solves for the answer
for sumNum in xrange(1,len(sumNums)):
    if sumNums[sumNum] == 0:
        totalTo89 += endChain(sumNum)
for i in xrange(568,10000000):
    if i%250000 == 0:
        print i
    if sumNums[sumSquareDigits(i)] == 89:
        totalTo89 += 1
print totalTo89
