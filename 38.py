# returns a list of all the digits in the specified number
def getDigits(number):
    x = []
    while number:
        x.append(number%10)
        number /= 10
    x.reverse()
    return x

# returns True if the concat. product of the specified number is 1-9 pandigital.
def concatProdPandigital(number):
    mult = 1
    digits = []
    while len(digits) < 9:
        digits.extend(getDigits(number*mult))
        mult += 1
    total = digits[:]
    total.sort()
    if total == [1,2,3,4,5,6,7,8,9]:
        concatProd = 0
        for i in range(0,9):
            concatProd += (10**(8-i))*digits[i]
        return concatProd
    return 0

# solves for the answer
answer = []
for num in range(1,10000):
    prod = concatProdPandigital(num)
    if prod != 0:
        answer.append(prod)
print max(answer)
