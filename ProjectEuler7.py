# returns the first 'a' prime numbers
def firstPrimes(a):
    x = [2]
    n = 2
    while len(x) < a:
        isPrime = True
        for j in x:
            if n%j == 0:
                isPrime = False
        if isPrime:
            x.append(n)
        n += 1
    return x

# solves for the answer
x = firstPrimes(10001)
print x[10000]
