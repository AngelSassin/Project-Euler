# returns all the primes whose values are less than the specified number.
def primesTo(a):
    allNumbers = set(range(2,a+1,1)) #set of all numbers needed to test
    list = []
    while len(allNumbers) > 0:
        prime = allNumbers.pop() 
        list.append(prime) #first number added is 2
        #remove all multiples of this prime number from the set of test numbers
        allNumbers -= set(range(prime,a+1,prime)) 
    return list

# solves for the answer.
primes = primesTo(2000000)
answer = sum(primes)
print answer
