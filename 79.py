# the keylog
file = open('keylog.txt','r')
keylog = file.read().split('\n')
keylog.remove('')

# returns the shortest possible secret passcode from the successful attempts
def shortestPossible(attempts):
    orders = set()
    possibleStart = [0]*10
    possibleEnd = [0]*10
    seen = [False]*10
    
    for attempt in attempts:
        orders.add((attempt[0],attempt[1]))
        orders.add((attempt[1],attempt[2]))
    for att in orders:
        a0 = int(att[0])
        a1 = int(att[1])
        seen[a0] = True
        seen[a1] = True
        possibleStart[int(att[1])] += 1
        possibleEnd[int(att[0])] += 1
    minRanges = [None]*10
    maxRanges = [None]*10
    for i in range(0,10):
        if seen[i]:
            minRanges[i] = possibleStart[i]
            maxRanges[i] = seen.count(True)-1-possibleEnd[i]
    solution = ''
    while len(solution) < (len(minRanges) - maxRanges.count(None)):
        copy = minRanges[:]
        while None in copy:
            copy.remove(None)
        first = None
        for i in range(0,10):
            if minRanges[i] == min(copy):
                if first == None or maxRanges[i] < maxRanges[first]:
                    first = i
        minRanges[first] = None
        solution += str(first)
    return solution

# solves for the answer
print shortestPossible(keylog)
