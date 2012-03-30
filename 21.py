import math

# returns the sum of proper divisors of the specified number.
def d(n):
    sum = 0
    for i in range(0,int(n**.5),1):
        if (n%(i+1) == 0):
            sum += (i+1)
            if i+1 != 1:
                sum += n/(i+1)
    return sum

# returns whether the specified number is amicable.
def isAmicable(num):
    a = d(num)
    b = d(a)
    return b == num and a != b

# solves for the answer.
answer = 0
for i in range(1,10000):
    if isAmicable(i):
        answer += i
print answer
