# returns the set of all integer combinations for a and b from 2 to the
#   specified number. The combinations all stem from a**b.
def getSequenceSet(num):
    totalSet = set()
    for a in range(2,num+1):
        for b in range(2,num+1):
            totalSet.add(a**b) #will not repeat values in a set! YAY!
    return totalSet

# solves for the answer.
answer = len(getSequenceSet(100))
print answer
