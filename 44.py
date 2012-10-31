def isPentagonal(num):
    isPent = (((24*num+1)**.5)+1)/6
    return isPent%1 == 0

def isPairPentagonal(t1,t2):
    if isPentagonal(t2-t1):
        if isPentagonal(t2+t1):
            return True
    return False
 
found = False
j = 0
while not found:
    j += 1
    pj = j*(3*j-1)/2
    for k in xrange(j,2500):
        pk = k*(3*k-1)/2
        if isPentagonal(pk-pj) and isPentagonal(pk+pj):
            print pk-pj
            found = True
            break

##def minDiffPentagonal():
##    a = 1
##    b = 2
##    minDiff = 0
##    minCouple = (0,0)
##    theTest = pentList[b]-pentList[a]
##    while minDiff == 0 or theTest < minDiff:
##        pA = pentList[a]
##        pB = pentList[b]
##        if b > 1000:
##            print 'past 1000'
##        if isPairPentagonal(a,b):
##            print 'DUDE, IT WORKED. ' + str(a) + ':' + str(pA) + ' | ' + str(b) + ':' + str(pB)
##            diff = pB-pA
##            if diff < minDiff or minDiff == 0:
##                minDiff = diff
##                minCouple = (pA,pB)
##        if minDiff != 0:
##            raw_input('a='+str(a)+' b='+str(b)+' | pA='+str(pA)+' pB='+str(pB)+' | minDiff='+str(minDiff)+' | couple='+str(minCouple))
##        if (pB-pA >= minDiff and minDiff != 0) or a == 1:
##            b += 1
##            a = b-1
##            pentList.append(b*(3*b-1)/2)
##            theTest = pentList[b]-pentList[a]
##        else:
##            a -= 1
##    return (minCouple,minDiff)
