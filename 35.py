import math

# returns all the primes up to the specified number
def primesTo(a):
    allNumbers = set(range(2,a+1,1))
    list = []
    while len(allNumbers) > 0:
        prime = allNumbers.pop()
        list.append(prime)
        allNumbers -= set(range(prime*2,a+1,prime))
    list.sort()
    return list

# returns whether the specified number is prime
def isPrime(a):
    if a == 0 or a == 1:
        return False
    for i in range(2,int(math.floor(math.sqrt(a)))+1):
        if a%i == 0:
            return False
    return True

# returns all rotations of the digits of the specified number
def getRotations(number):
    number = str(number)
    rotations = []
    for z in range(0,len(number)):
        number = number[1:len(number)] + number[0]
        rotations.append(int(number))
    return rotations

# returns True if the specified number is circular prime
def isCircularPrime(number):
    rotations = getRotations(number)
    for n in rotations:
        if not isPrime(n):
            return False
    return True

# returns all circular primes below the specified number
def getCircularPrimes(below):
    cPrimes = [0]*below
    for i in primesTo(below):
        if isCircularPrime(i):
            cPrimes[i] = 1
    return cPrimes

# solves for the answer
answer = getCircularPrimes(1000000)
print sum(answer)
