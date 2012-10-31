# returns the greatest common divisor of the two specified numbers
def gcd(a,b):
    if a%b == 0:
        return b
    else:
        return gcd(b,a%b)

# returns the product of all items in a list
def product(theList):
    product = 1
    for i in theList:
        product *= i
    return product

# returns True if the specified fraction can equal another fraction obtained
#   by removing one specific digit. 
def isTrueRemoval(numer,denom):
    if numer%10 == 0 and denom%10 == 0:
        return False
    removal = False
    for i in range(0,10):
        removNum = removeDigit(numer,i)
        removDen = removeDigit(denom,i)
        if removDen != 0 and (numer != removNum or denom != removDen):
            if numer*1.0/denom == removNum*1.0/removDen:
                removal = True
    return removal

# returns a number obtained by removing a digit from the specified number
def removeDigit(number,digit):
    original = number
    sum = 0
    removed = 0
    while number:
        numDigit = number%10
        if numDigit != digit:
            sum += (10**removed)*numDigit
            removed += 1
        number /= 10
    return sum

# solves for the answer
numerators = []
denominators = []
for denominator in range(10,100):
    for numerator in range(10,denominator):
        if isTrueRemoval(numerator,denominator):
            numerators.append(numerator)
            denominators.append(denominator)
productNum = product(numerators)
productDen = product(denominators)
answer = productDen/gcd(productNum,productDen)
print answer
