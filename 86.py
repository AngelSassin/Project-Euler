sq = range(100001)
for i in xrange(len(sq)):
    sq[i] = sq[i]**2
print 'done'

def solves(x,y,z):
    paths = [sq[x]+sq[y+z],sq[x+y]+sq[z],sq[x+z]+sq[y]]
    m = min(paths)**.5
    return m%1 == 0

def cMaxLen(n):
    total = 0
    for i in xrange(1,n+1):
        for j in xrange(i,n+1):
            if solves(i,j,n):
                total += 1
    return total

# solves for the answer
M = 0
total = 0
while total < 1000000:
    M += 1
    total += cMaxLen(M)
print M
