import itertools

def add(x,y):
    return x+y

def sub1(x,y):
    return x-y

def sub2(x,y):
    return y-x

def mult(x,y):
    return x*y

def div1(x,y):
    if y == 0:
        return None
    return x*1.0/y

def div2(x,y):
    if x == 0:
        return None
    return y*1.0/x

operations = [add,sub1,sub2,mult,div1,div2]

def performCalcs(a,b,c,d):
    answers = [False]*9*8*7*7
    combs = itertools.permutations([a,b,c,d],4)
    for w in combs:
        for x in operations:
            solx = x(w[0],w[1])
            for y in operations:
                if solx == None:
                    break
                soly = y(solx,w[2])
                for z in operations:
                    if soly == None:
                        break
                    solz = z(soly,w[3])
                    if solz != None and solz%1 == 0 and solz > 0:
                        answers[int(solz)] = True
    length = 1
    while answers[length]:
        length += 1
    return length-1

# solves for the answer
largest = 0
answer = '1234'
for a in xrange(1,7):
    for b in xrange(a+1,8):
        for c in xrange(b+1,9):
            for d in xrange(c+1,10):
                x = performCalcs(a,b,c,d)
                if x > largest:
                    largest = x
                    answer = str(a)+str(b)+str(c)+str(d)
print str(largest) + ' - ' + answer
