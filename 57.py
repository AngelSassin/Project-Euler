# returns the number of times the numerator has more digits than denominator
#   in the specified number of iterations of the fraction.
def getNumLargerNumer(iterations):
    count = 0
    numerator = 3
    denominator = 2
    for i in range(1,iterations):
        numerator += denominator
        temp = numerator
        numerator = denominator
        denominator = temp
        numerator += denominator
        if len(str(numerator)) > len(str(denominator)):
            count += 1
    return count

# solves for the answer
answer = getNumLargerNumer(1000)
print answer
    
    
