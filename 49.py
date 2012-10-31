import math

# returns True if the specified number is prime
def isPrime(a):
    if a <= 1:
        return False
    for i in range(2,int(math.floor(math.sqrt(a)))+1):
        if a%i == 0:
            return False
    return True

# returns True if the number fits the arithmetic sequence
def sequencePermutation(number):
    num1 = []
    num2 = []
    num3 = []
    for i in str(number):
        num1.append(i)
    for i in str(number+3330):
        num2.append(i)
    for i in str(number+6660):
        num3.append(i)
    num1.sort()
    num2.sort()
    num3.sort()
    if num1 == num2 and num1 == num3:
        return True
    return False

# returns the list of all 4-digit primes that fit the arithmetic sequence
def findPermPrimes():
    x = []
    for i in range(1000,10000):
        if sequencePermutation(i):
            if isPrime(i) and isPrime(i+3330) and isPrime(i+6660):
                x.append(i)
    return x

# solves for the answer
answer = findPermPrimes()[1]
print str(answer) + str(answer+3330) + str(answer+6660)
