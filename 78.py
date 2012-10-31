pn = [-1]*50000000
pn[0] = 1
print "DONE"

def P(n):
    if n < 0:
        return 0
    x = pn[n]
    if x != -1:
        return x
    total = 0
    for k in xrange(1,n+1):
        total += ((-1)**(k+1))*(P(n-((k*(3*k-1))/2))+P(n-((k*(3*k+1))/2)))
    pn[n] = total
    return total

# solves for the answer
x = 0
p = 1
while p%1000000 != 0:
    x += 1
    p = P(x)
print str(x) + ' - ' + str(p)
