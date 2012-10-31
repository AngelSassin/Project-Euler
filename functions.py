import math
import prime
import math
import random
from fractions import Fraction

# returns the greatest common divisor of the two specified numbers
def gcd(a,b):
    if a%b == 0:
        return b
    else:
        return gcd(b,a%b)

# returns the least common multiple of the two specified numbers
def lcm(a,b):
    return (a*b)/gcd(a,b)

# returns the list of all the factors of the specified number
def factors(a):
    x = []
    for i in range(1,int(math.floor(math.sqrt(a)))+1):
        if a%i == 0:
            x.append(i)
            if (a/i != i):
                x.append(a/i)
    x.sort()
    return x

# returns the number of positive integers relatively prime to specified number
def phi(n):
    assert n > 0
    if n != 1:
        answer = n
        pFactors = prime.primeFactors(n)
        pFactors = set(pFactors)
        for p in pFactors:
            answer *= 1 - 1.0/p
        return answer
    return 1

# Returns a list of the phi of each number to n represented by the index of the list
def phiSieve(n):
    theList = range(n+1)
    theList[0] = 0
    theList[1] = 1
    for i in xrange(2,len(theList)):
        if i == theList[i]:
            x = i*2
            while x < len(theList):
                theList[x] *= 1 - 1.0/i
                x += i
            theList[i] -= 1
    return theList

def fourier(n):
    answer = 0
    for k in xrange(1,n+1):
        answer += gcd(k,n)*math.cos(2*math.pi*k/n)
    return answer

def pollardRho(N):
    if N%2==0:
        return 2
    x = random.randint(1, N-1)
    y = x
    c = random.randint(1, N-1)
    g = 1
    while g==1:         
        x = ((x*x)%N+c)%N
        y = ((y*y)%N+c)%N
        y = ((y*y)%N+c)%N
        g = gcd(abs(x-y),N)
    return g

def primePollardRho(x):
    def primePollardRhoHelper(factors,N):
        fact = N
        while fact == N:
            fact = pollardRho(N)
        if fact == 1:
            factors.append(N)
        else:
            factors = primePollardRhoHelper(factors,fact)
            factors = primePollardRhoHelper(factors,N/fact)
        return factors
    return primePollardRhoHelper([],x)
