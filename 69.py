import math

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
primes = primesTo(1000)

# solves for the answer
nHigh = 1000000
answer = 1
for p in primes:
    if answer*p > nHigh:
        break
    answer *= p
print answer
