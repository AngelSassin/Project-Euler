# the possible ways to make a triangle with the indexed perimeter
primitiveWays = [0]*1500001
ways = [0]*1500001

# returns the greatest common divisor of the two specified numbers
def gcd(a,b):
    if a%b == 0:
        return b
    else:
        return gcd(b,a%b)

# counts the number of possible ways to make primitive right-triangles
def getPrimitiveWays():
    for n in xrange(1,615):
        for m in xrange(n+1,1227):
            if (m%2==0 or n%2==0) and gcd(m,n) == 1:
                c = m**2+n**2
                a = m**2-n**2
                b = 2*m*n
                p = a+b+c
                if p < len(primitiveWays):
                    primitiveWays[p] += 1

# solves for the answer
getPrimitiveWays()
for i in xrange(12,len(primitiveWays),2):
    for j in xrange(i,len(ways),i):
        ways[j] += primitiveWays[i]
count = 0
for i in xrange(len(ways)):
    if ways[i] == 1:
        count += 1
print count
