triangles = [0,1,3,6,10]
pentagons = [0,1,5,12,22]
hexagons = [0,1,6,15,28]

# returns the list of the first n numbers that are triangle, pentagonal, and
#   hexagonal
def findTriPentHex(num):
    x = []
    t = 1
    p = 1
    h = 1
    tri = triangles[t]
    pnt = pentagons[p]
    hx = hexagons[h]
    while len(x) < num:
        if t >= len(triangles):
            triangles.append(t*(t+1)/2)
        tri = triangles[t]
        if pnt < tri:
            p += 1
            pentagons.append(p*(3*p-1)/2)
            pnt = pentagons[p]
        if hx < tri:
            h += 1
            hexagons.append(h*(2*h-1))
            hx = hexagons[h]
        if tri == pnt and tri == hx:
            x.append(tri)
        t += 1
    return x

# solves for the answer
answer = findTriPentHex(3)
print answer[2]
        
