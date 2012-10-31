# returns the number of solutions of a right triangle with certain perimeter.
def perimeterSolutions(perimeter):
    solutions = 0
    for a in range(0,(perimeter+1)/4):
        for b in range(a,(perimeter+1)/2):
            c = (a**2+b**2)**.5
            if c%1 == 0:
                c = int(c)
                if a+b+c == perimeter:
                    solutions += 1
    return solutions

# solves for the answer
answer = 0
maxSolutions = 0
for p in range(1,1001):
    solutions = perimeterSolutions(p)
    if solutions > maxSolutions:
        answer = p
        maxSolutions = solutions
print answer
