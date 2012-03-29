import math

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

# returns the first triangle number to have at least the specified
#   number of divisors.
def getFirstTriangleWithDivisors(divs):
    triangle = 0
    iteration = 1
    while len(factors(triangle)) <= divs:
        triangle += iteration
        iteration += 1
    return triangle

# solves for the answer
answer = getFirstTriangleWithDivisors(500)
print answer
