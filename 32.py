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

# returns a list of all the digits in the specified number
def getDigits(number):
    x = []
    while number:
        x.append(number%10)
        number /= 10
    x.sort()
    return x

# returns True if multiplicand/multiplier/product identity is 1-9 pandigital.
def isIdentityPandigital(number):
    factorList = factors(number)
    digits = getDigits(number)
    isPandigital = False
    for fact1 in factorList:
        total = digits[:]
        fact2 = number/fact1
        digits1 = getDigits(fact1)
        digits2 = getDigits(fact2)
        total.extend(digits1)
        total.extend(digits2)
        total.sort()
        if total == [1,2,3,4,5,6,7,8,9]:
            isPandigital = True
    return isPandigital

# solves for the answer.
pandigitals = []
for num in range(1000,10000):
    if isIdentityPandigital(num):
        pandigitals.append(num)
answer = sum(pandigitals)
print answer
