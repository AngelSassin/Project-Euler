import itertools

# the sets
sets = open('sets.txt', 'r')
sets = sets.read().split('\n')
for i in xrange(len(sets)):
    sets[i] = sets[i].split(',')
    for j in xrange(len(sets[i])):
        sets[i][j] = int(sets[i][j])
    sets[i] = set(sets[i])

# checks whether the specified set is a special sum set.
def isSpecialSumSet(theSet):
    # combinations here
    for i in xrange(1,len(theSet)+1):
        possibleB = itertools.combinations(theSet,i)
        for bSet in possibleB:
            newSet = theSet - set(bSet)
            for j in xrange(1,len(newSet)+1):
                possibleC = itertools.combinations(newSet,j)
                for cSet in possibleC:
                    if sum(bSet) == sum(cSet):
                        return False
                    if len(bSet) > len(cSet):
                        if sum(bSet) < sum(cSet):
                            return False
    return True

# solves for the answer
answer = []
for s in sets:
    if isSpecialSumSet(s):
        answer.append(sum(s))
print sum(answer)
