# returns the sum of the digits in the number each to the specified power.
def getDigitPowerSum(number,power):
    digits = []
    while number > 0:
        digits.append(number%10)
        number /= 10
    sum = 0
    for i in digits:
        sum += i**power
    return sum

# If we check a 6-digit number, the maximum possible sum of powers
# is 354294. If we check any 7-digit number, the maximum possible sum
# doesn't even reach 7 digits. It is impossible for any number greater
# than 354294 to be written as the sum of fifth powers of its digits.

# solves for the answer
works = []
for i in range(10,354294): 
    if getDigitPowerSum(i,5) == i:
        works.append(i)
answer = sum(works)
print answer
