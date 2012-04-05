import math

# returns True if the number is prime
def isPrime(a):
    numFactors = 0
    for i in range(1,int(math.floor(a**.5))+1):
        if a%i == 0:
            numFactors += 1
        if numFactors > 1:
            return False
    return True

# returns the product of the two integers a and b
def getQuadProduct():
    maxPrimes = 0
    maxProduct = 0
    for a in range(-999,1000,1):
        for b in range(-999,1000,1):
            n = 0
            while n**2 + a*n + b >= 0:
                if isPrime(n**2 + a*n + b):
                    n += 1
                else:
                    break
            if n > maxPrimes:
                maxPrimes = n
                maxProduct = a*b
    return maxProduct

# solves for the answer
answer = getQuadProduct()
print answer
