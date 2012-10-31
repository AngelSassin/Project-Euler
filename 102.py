import math

# the triangles
tri = open('triangles.txt','r')
tri = tri.read().split('\n')
del tri[len(tri)-1]
for i in xrange(len(tri)):
    tri[i] = tri[i].split(',')
    for j in xrange(6):
        tri[i][j] = int(tri[i][j])

# the cross product of two vectors
def cross(a, b):
    return [a[1]*b[2] - a[2]*b[1],
            a[2]*b[0] - a[0]*b[2],
            a[0]*b[1] - a[1]*b[0]]

# the difference between two vectors
def minus(a, b):
    return [a[0] - b[0],
            a[1] - b[1],
            a[2] - b[2]]

# the dot product of two vectors
def dot(a, b):
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]

# tells whether 2 points are on the same side of a line
def sameSide(p1,p2,a,b):
    c1 = cross(minus(b,a), minus(p1,a))
    c2 = cross(minus(b,a), minus(p2,a))
    return dot(c1,c2) >= 0

# tells whether a the specified triangle contains the origin
def hasOrigin(t):
    a = [t[0],t[1],0]
    b = [t[2],t[3],0]
    c = [t[4],t[5],0]
    o = [0,0,0]
    return sameSide(o,c, a,b) and sameSide(o,a, b,c) and sameSide(o,b, a,c)

# solves for the answer
answer = 0
for t in tri:
    if hasOrigin(t):
        answer += 1
print answer
