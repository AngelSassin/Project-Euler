import itertools

def getOuter(p, gon):
    used = [0]*gon*2
    for x in p:
        used[x-1]=1
    left = []
    for x in range(len(used)):
        if used[x] == 0: left.append(x+1)
    left.sort()
    left.reverse()
    return left

def getSolutionSets(gon):
    solutions = []
    possible = range(1,2*gon+1)
    perms = itertools.permutations(possible,gon)
    for perm in perms:
        perm = list(perm)
        outer = getOuter(perm,gon)
        theSum = perm[0] + perm[1] + outer[0]
        works = True
        for i in xrange(gon):
            if perm[i]+perm[(i+1)%gon]+outer[i] != theSum:
                works = False
        if works:
            index = outer.index(min(outer))
            sol = []
            sol2 = []
            for i in xrange(gon,0,-1):
                sol.append(outer[(i+index)%gon])
                sol.append(perm[(i+index+1)%gon])
                sol.append(perm[(i+index)%gon])
                sol2.append(outer[(gon-i+index)%gon])
                sol2.append(perm[(gon-i+index)%gon])
                sol2.append(perm[(gon-i+index+1)%gon])
            solutions.append(sol)
            solutions.append(sol2)
    return solutions

# returns the maximum 16-digit concatinated solution
def maxConcat(possible):
    for sol in xrange(len(possible)):
        num = ''
        for i in possible[sol]:
            num += str(i)
        if len(num) == 16:
            possible[sol] = int(num)
        else: possible[sol] = 0
    return max(possible)
        
# solves for the answer
solutions = getSolutionSets(5)
answer = maxConcat(solutions)
print answer
