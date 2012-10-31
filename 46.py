# returns all the primes up to 'a'
def primesTo(a):
    allNumbers = set(range(2,a+1,1))
    list = []
    while len(allNumbers) > 0:
        prime = allNumbers.pop()
        list.append(prime)
        allNumbers -= set(range(prime*2,a+1,prime))
    list.sort()
    return list

# the primes
primes = primesTo(10000)

# returns True if the number can be written as a prime plus twice a square
def isSumPrime2Square(number):
    for i in range(0,int(number**.5)):
        test = number
        test -= 2*i**2
        if test in primes:
            return True
    return False

# finds the first odd composite number that is not a prime plus twice a square
def findFalse():
    oddComp = range(3,10000,2)
    for i in primes[1:len(primes)]:
        oddComp.remove(i)
    for num in oddComp:
        if not isSumPrime2Square(num):
            return num
    return 0

# solves for the answer
answer = findFalse()
print answer
