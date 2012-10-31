import functions

def hashDigits(n):
    hDig = []
    while n:
        hDig.append(n%10)
        n /= 10
    hDig.sort()
    return hDig
'''
def hashDigits(n):
    hDigProd = 1
    hDigSum = 0
    while n:
        temp = (n%10)+10
        hDigProd *= temp
        hDigSum += temp
        n /= 10
    return (hDigProd,hDigSum)
'''
        
def isPerm(i, j):
    return hashDigits(i) == hashDigits(j)

theList = range(10000000)
theList[0] = 2
theList[1] = 2
for i in xrange(2,10000000):
    if i == theList[i]:
        x = i*2
        while x < 10000000:
            theList[x] *= 1 - 1.0/i
            x += i
        theList[i] -= 1
    if isPerm(i,int(theList[i])):
        theList[i] = i*1.0/theList[i]
    else:
        theList[i] = 2
    if i%10000 == 0:
        print i
minRatio = 2
minIndex = 0
for i in xrange(10000000):
    if theList[i] < minRatio:
        minRatio = theList[i]
        minIndex = i
print str(minIndex) + ' - ' + str(minRatio)
