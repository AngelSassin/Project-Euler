import math

# returns the factorial of a number
def fact(x):
    return math.factorial(x)

# returns the value of n-combination-r
def combination(n,r):
    return fact(n)/(fact(r)*fact(n-r))

# solves for the answer
answer = 0
for n in range(1,101):
    for r in range(0,n+1):
        if combination(n,r) > 1000000:
            answer += 1
print answer
