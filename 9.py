import math

# returns the first integer product of the Pythagorean triplet numbers
#   whose sum is equal to the specified number.
def getProductPythagSum(sum):
    for a in range(0,500):
        for b in range(0,500):
            c = (a**2+b**2)**.5
            if a+b+c == 1000:
                return int(a*b*c)

# solves for the answer.
answer = getProductPythagSum(1000)
print answer
            
