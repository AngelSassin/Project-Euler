# returns the digits of the specified number.
def getDigits(number):
    digits = []
    while number > 0:
        digits.append(number%10)
        number /= 10
    return digits

# solves for the answer
answer = sum(getDigits(2**1000))
print answer
