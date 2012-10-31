import prime
import search
import string
import itertools

primes = prime.primesTo(10000)

# returns True if concatinating the two numbers in any order results in a prime
def ccatPrimes(a,b):
    return prime.isPrime(int(str(a)+str(b))) and prime.isPrime(int(str(b)+str(a)))

def findAnswer():
    minSum = 100000
    for a in primes:
        for b in primes:
            if a+b < minSum and ccatPrimes(a,b):
                for c in primes:
                    if a+b+c < minSum and ccatPrimes(a,c) and ccatPrimes(b,c):
                        for d in primes:
                            if a+b+c+d < minSum and ccatPrimes(a,d) and ccatPrimes(b,d) and ccatPrimes(c,d):
                                print str(a)+","+str(b)+","+str(c)+","+str(d)
                                for e in primes:
                                    if a+b+c+d+e < minSum and ccatPrimes(a,e) and ccatPrimes(b,e) and ccatPrimes(c,e) and ccatPrimes(d,e):
                                        minSum = a+b+c+d+e
                                        print str(a)+","+str(b)+","+str(c)+","+str(d)+","+str(e)+" - "+str(minSum)
    return minSum

def findAnswer2():
    combs = {}
    for a in primes:
        combs[a] = []
        for b in primes:
            if ccatPrimes(a,b):
                combs[a].append(b)
    for i in combs:
        for j in combs[i]:
            for k in combs[j]:
                if search.searchList(combs[i],k):
                    for l in combs[k]:
                        if search.searchList(combs[i],l):
                            if search.searchList(combs[j],l):
                                for m in combs[l]:
                                    if search.searchList(combs[j],m):
                                        if search.searchList(combs[k],m):
                                            if search.searchList(combs[m],i):
                                                return i+j+k+l+m
                                                

# solves for answer
print findAnswer2()
