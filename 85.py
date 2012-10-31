import math

def countRectangles(w, h):
    total = 0
    for rw in xrange(1,w+1):
        for rh in xrange(1,h+1):
            total += (w-rw+1)*(h-rh+1)
    return total

# solves for the answer
THE_NUM = 2000000
w = 1
h = 1
a = THE_NUM
ww = 1
hh = 1
aa = countRectangles(ww,hh)
xx = THE_NUM-aa
if xx < 0:
    xx *= -1
while aa <= THE_NUM:
    while aa <= THE_NUM:
        if xx < a:
            a = xx
            w = ww
            h = hh
        hh += 1
        aa = countRectangles(ww,hh)
        xx = THE_NUM-aa
        if xx < 0:
            xx *= -1
    ww += 1
    hh = ww
    aa = countRectangles(ww,hh)
    xx = THE_NUM-aa
    if xx < 0:
        xx *= -1
print w*h

        
