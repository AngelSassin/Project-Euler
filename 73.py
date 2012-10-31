def fractions(x):
    added = [[False]]*(x+1)
    added[0] = None
    for i in xrange(1,x+1):
        added[i] = added[i]*i
    fList = []
    for d in xrange(2,x+1):
        for n in xrange(int(d/3.0)+1,int(d/2.0 + .5)):
            if not added[d][n]:
                fList.append(n*1.0/d)
                i = 1
                while d*i <= x:
                    added[d*i][n*i] = True
                    i += 1
    fList.sort()
    return fList

# solves for the answer
fList = fractions(12000)
print len(fList)
