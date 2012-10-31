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

# returns the longest list of the consecutive primes with a prime sum
def tehAnswer(highest):
    primes = primesTo(highest)
    start = 0
    top = 1
    maximum = [2]
    while sum(primes[start:top]) < highest:
        top += 1
    while top - start >= len(maximum):
        end = top
        while end - start >= len(maximum):
            theRange = primes[start:end]
            if sum(primes[start:end]) in primes:
                maximum = primes[start:end]
                break
            end -= 1
        start += 1
    return maximum

# solves for the answer
answer = sum(tehAnswer(1000000))
print answer
        
            
        
        



