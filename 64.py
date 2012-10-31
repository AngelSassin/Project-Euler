def oneExpansion(integer,root,add,den):
    i = int(((root**.5)+add)/((root-add**2)/den))
    den = ((root-add**2)/den)
    add = den*i - add
    return (i,root,add,den)

def doExpansion(root):
    if root**.5 == int(root**.5):
        return 0
    results = [(int(root**.5),root,int(root**.5),1)]
    results = [oneExpansion(results[0][0],results[0][1],results[0][2],results[0][3])]
    result = results
    results = [oneExpansion(results[0][0],results[0][1],results[0][2],results[0][3])]
    done = 1
    while result != results:
        done += 1
        results = [oneExpansion(results[0][0],results[0][1],results[0][2],results[0][3])]
    return done

# solves for the answer
count = 0
for i in xrange(10001):
    if doExpansion(i) % 2 == 1:
        count += 1
print count
