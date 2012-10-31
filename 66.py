import math
from fractions import Fraction
from decimal import Decimal

def findX(D):
    if math.sqrt(D)%1 == 0:
        return 0
    y = 1
    while True:
        x = math.sqrt(D*y*y + 1)
        if x%1 == 0:
            return x
        y += 1

def oneExpansion(integer,root,add,den):
    i = int(((root**.5)+add)/((root-add**2)/den))
    den = ((root-add**2)/den)
    add = den*i - add
    return (i,root,add,den)

def giveExpansions(D):
    sqrt = D**.5
    if sqrt == int(sqrt):
        return None
    r0 = (int(sqrt),D,int(sqrt),1)
    res = [r0]
    exp0 = oneExpansion(res[0][0],res[0][1],res[0][2],res[0][3])
    res.append(exp0)
    ln = 1
    while ln == 1 or res[ln] != exp0:
        res.append(oneExpansion(res[ln][0],res[ln][1],res[ln][2],res[ln][3]))
        ln += 1
    if len(res)%2 == 1:
        tln = ln
        while tln == ln or res[ln] != exp0:
            res.append(oneExpansion(res[ln][0],res[ln][1],res[ln][2],res[ln][3]))
            ln += 1
    answer = []
    end = len(res)-2
    for i in xrange(end):
        answer.append(res[i][0])
    return answer

def findXY(D):
    exp = giveExpansions(D)
    if exp == None:
        return None
#    exp = exp[:len(exp)-1]
    dec = Fraction(exp[len(exp)-1])
    for i in xrange(len(exp)-1,0,-1):
        dec = Fraction(exp[i-1]) + Fraction(1/dec)
    return dec

# solves for the answer
maxX = 0
maxD = 0
for D in xrange(1,1001):
    answer = findXY(D)
    if answer != None:
        if answer.numerator > maxX:
            maxX = answer.numerator
            maxD = D
print maxD
