import math

# returns the digits of the specified number.
def getDigits(number):
    digits = []
    while number > 0:
        digits.append(number%10)
        number /= 10
    return digits

# solves for the answer.
factorial = math.factorial(100)
answer = sum(getDigits(factorial))
print answer
