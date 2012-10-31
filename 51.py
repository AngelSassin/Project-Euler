import prime
import search
import clock
import string

# THE PRIMES #
primes = prime.primesTo(1000000)

# returns the largest family for the specified prime
def getFamily(n):
    digits = len(str(n))
    family = []
    original = n
    for i in xrange(0,10):
        tempFamily = []
        n = str(original)
        tempOriginal = string.replace(n,str(i),"*")
        if string.count(tempOriginal,"*") == 3:
            for j in xrange(0,10):
                n = tempOriginal
                tempNum = int(string.replace(n,"*",str(j)))
                if search.searchList(primes,tempNum):
                    tempFamily.append(tempNum)
            if (len(tempFamily) > len(family) or (len(tempFamily) != 0 and len(tempFamily) == len(family) and tempFamily[0] < family[0])) and len(str(tempFamily[0])) == digits:
                family = tempFamily
    return family

# solves for the answer
for i in primes:
    answer = getFamily(i)
    if len(answer) == 8:
        print answer[0]
        break
        
