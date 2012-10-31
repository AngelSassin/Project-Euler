import math

def hasRightAngle(x1,y1,x2,y2):
    if x1 == 0 and y1 == 0 or x2 == 0 and y2 == 0 or x1 == x2 and y1 == y2:
        return False
    ss1 = (x1**2 + y1**2)
    ss2 = (x2**2 + y2**2)
    ss3 = ((x1-x2)**2 + (y1-y2)**2)
    return ss1+ss2==ss3 or ss2+ss3==ss1 or ss3+ss1==ss2

# solves for the answer
LIMIT = 50
total = 0
for x1 in xrange(LIMIT+1):
    for y1 in xrange(LIMIT+1):
        for x2 in xrange(LIMIT+1):
            for y2 in xrange(LIMIT+1):
                if hasRightAngle(x1,y1,x2,y2):
                    total += 1
print total/2
