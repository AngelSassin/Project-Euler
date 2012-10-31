import math

# The greatest number equal to a sum of factorials of single-digit numbers
#   is 2540160, which is the sum of the factorials of the digits of 9999999.

# the factorials
factorials = []
for i in range(0,10):
    factorials.append(math.factorial(i))

# returns the sum of the factorials of the digits of the specified number
def sumDigitFact(number):
    digits = []
    while number:
        digits.append(number%10)
        number /= 10
    if len(digits) == 1:
        return 0
    total = 0
    for n in digits:
        total += factorials[n]
    return total

def getCuriousNumbers(maximum):
    x = []
    for number in range(0,maximum):
        if number == sumDigitFact(number):
            x.append(number)
    return x

# solves for the answer
answer = getCuriousNumbers(1000000)
print sum(answer)
