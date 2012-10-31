import math

# returns the list of all the prime factors of the specified number
def primeFactors(a):
    x = []
    # The loop only appends the first prime number to x, then breaks.
    for i in range(2,int(math.floor(math.sqrt(a)))+1):
        if a%i == 0:
            x.append(i)
            break
    if len(x) == 0:
        return [a]
    for n in primeFactors(a/x[0]):
        x.append(n)
    return x

# returns the list of the first c consecutive numbers to have p primes
def hasDistinctPrimes(p,c):
    number = 2
    found = []
    while len(found) < c:
        if len(set(primeFactors(number))) >= p:
            found.append(number)
        else:
            del found[:]
        number += 1
    return found

# solves for the answer
answer = hasDistinctPrimes(4,4)
print answer

