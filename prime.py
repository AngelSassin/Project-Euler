import math
import random

# returns list of primes less than 'n'
def primesTo(n): 
    if n==2: return [2]
    elif n<2: return []
    s=range(3,n+1,2)
    mroot = n ** 0.5
    half=(n+1)/2-1
    i=0
    m=3
    while m <= mroot:
        if s[i]:
            j=(m*m-3)/2
            s[j]=0
            while j<half:
                s[j]=0
                j+=m
        i=i+1
        m=2*i+3
    return [2]+[x for x in s if x]
 
def isPrime(n,num = 20):
    assert n >= 2
    if n == 2: # special case 2
        return True
    if n % 2 == 0: # ensure n is odd
        return False
    s = 0 
    d = n-1 # write n-1 as 2**s * d
    while True: # repeatedly try to divide n-1 by 2
        quotient, remainder = divmod(d, 2)
        if remainder == 1:
            break
        s += 1
        d = quotient
    assert(2**s * d == n-1)
    def try_composite(a): # test the base a to see whether it is a witness for the compositeness of n
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True # n is definitely composite
    for i in range(num):
        a = random.randrange(2, n)
        if try_composite(a):
            return False
    return True # no base tested showed n as composite

# returns the list of all the prime factors of the specified number
def primeFactors(a):
    x = []
    # The loop only appends the first prime number to x, then breaks.
    for i in xrange(2,int(a**.5)+1):
        if a%i == 0:
            x.append(i)
            break
    if len(x) == 0:
        return [a]
    for n in primeFactors(a/x[0]):
        x.append(int(n))
    return x

# all the primes in the sieve algorithm
def sievePrimes():
    D = {}
    q = 2
    while q < 10000000000:
        if q not in D:
            yield q        
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1
