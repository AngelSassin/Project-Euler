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

# solves for the answer
list = primeFactors(600851475143)
answer = list[len(list)-1]
print answer
