def getPolys(sides,digits):
    polys = []
    def fun(ix):
        if sides == 3:
            return ix*(ix+1)/2
        if sides == 4:
            return ix*ix
        if sides == 5:
            return ix*(3*ix-1)/2
        if sides == 6:
            return ix*(2*ix-1)
        if sides == 7:
            return ix*(5*ix-3)/2
        if sides == 8:
            return ix*(3*ix-2)
        return ix
    n = 1
    num = 0
    while len(str(num)) <= digits:
        num = fun(n)
        if len(str(num)) == digits:
            if str(num)[2] != "0":
                polys.append(num)
        n += 1
    return polys

triangles = getPolys(3,4)
squares = getPolys(4,4)
pentagons = getPolys(5,4)
hexagons = getPolys(6,4)
heptagons = getPolys(7,4)
octagons = getPolys(8,4)

def isPair(n1,n2):
    return str(n2)[0:2] == str(n1)[2:4]

def method3(total, original, value):
    if value == None:
        for p3 in triangles:
            methods = [method4,method5,method6,method7,method8]
            for m in methods:
                temp = methods[:]
                temp.remove(m)
                m(p3, p3, p3, temp)
    elif isPair(value,original):
        print total

def method4(total, original, value, methods):
    for p4 in squares:
        if isPair(value,p4):
            if len(methods) == 0:
                method3(total+p4, original, p4)
            else:
                for m in methods:
                    temp = methods[:]
                    temp.remove(m)
                    m(total+p4, original, p4, temp)

def method5(total, original, value, methods):
    for p5 in pentagons:
        if isPair(value,p5):
            if len(methods) == 0:
                method3(total+p5, original, p5)
            else:
                for m in methods:
                    temp = methods[:]
                    temp.remove(m)
                    m(total+p5, original, p5, temp)

def method6(total, original, value, methods):
    for p5 in hexagons:
        if isPair(value,p5):
            if len(methods) == 0:
                method3(total+p5, original, p5)
            else:
                for m in methods:
                    temp = methods[:]
                    temp.remove(m)
                    m(total+p5, original, p5, temp)

def method7(total, original, value, methods):
    for p5 in heptagons:
        if isPair(value,p5):
            if len(methods) == 0:
                method3(total+p5, original, p5)
            else:
                for m in methods:
                    temp = methods[:]
                    temp.remove(m)
                    m(total+p5, original, p5, temp)

def method8(total, original, value, methods):
    for p5 in octagons:
        if isPair(value,p5):
            if len(methods) == 0:
                method3(total+p5, original, p5)
            else:
                for m in methods:
                    temp = methods[:]
                    temp.remove(m)
                    m(total+p5, original, p5, temp)

# solves for the answer
method3(0,0,None)
