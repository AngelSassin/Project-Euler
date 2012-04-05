import time

# returns the number that yeilds the highest recurring cycle
def getCycle(num):
    maxNumber = 0
    maxLength = 0
    for number in range(1,num):
        r = 1
        r0 = 0
        for i in range(0,10):
            r = (10*r)%number
        r0 = r
        r = (10*r)%number
        length = 1
        while r != r0:
            r = (10*r)%number
            length += 1
        if length > maxLength:
            maxLength = length
            maxNumber = number
    return maxNumber

# solves for the answer
answer = getCycle(1000)
print answer
