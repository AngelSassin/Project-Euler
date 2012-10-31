import prime

# the base/exponent pairs
pairs = open('base_exp.txt', 'r')
pairs = pairs.read().split('\n')
for i in xrange(len(pairs)):
    pairs[i] = pairs[i].split(',')
    pairs[i][0] = int(pairs[i][0])
    pairs[i][1] = int(pairs[i][1])

# compares the two pairs
def firstGreater(pair1,pair2):
    return pair1[0] > pair2[0]**(pair2[1]*1.0/pair1[1])






# solves for the answer
largest = pairs[0]
index = 0
for i in xrange(len(pairs)):
    x = pairs[i]
    if firstGreater(x,largest):
        largest = x
        index = i
print str(index+1) + ' - ' + str(largest)
