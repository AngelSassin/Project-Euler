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

# returns True if the specified number is prime
def isPrime(a):
    if a <= 1:
        return False
    for i in range(2,int(math.floor(math.sqrt(a)))+1):
        if a%i == 0:
            return False
    return True

def truncatable(number):
    original = number
    while number:
        number = int(number)
        if not isPrime(number):
            return False
        number = str(number)
        number = number[0:len(number)-1]
    number = original
    while number:
        number = int(number)
        if not isPrime(number):
            return False
        number = str(number)
        number = number[1:len(number)]
    return True

# solves for the answer
answer = []
for i in primesTo(1000000):
    if i >= 10:
        if truncatable(i):
            answer.append(i)
        if len(answer) == 11:
            break
print sum(answer)
