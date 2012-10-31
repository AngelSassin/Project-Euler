# returns the digits in a number
def digits(number):
    d = []
    while number:
        d.append(number%10)
        number /= 10
    return d

# returns the maximum digital sum of the numbers in the list
def getGreatestDigitalSum(theList):
    maximum = 0
    for i in theList:
        s = sum(digits(i))
        if s > maximum:
            maximum = s
    return maximum

# solves for the answer
possible = []
for a in range(0,100):
    for b in range(0,100):
        possible.append(a**b)
answer = getGreatestDigitalSum(possible)
print answer
