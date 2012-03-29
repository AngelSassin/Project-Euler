# returns all Fibonacci numbers whose values do not exceed four million.
def getFibonacciNumbers():
    x = [1,2]
    nextValue = x[len(x)-1] + x[len(x)-2]
    while nextValue <= 4000000:
        x.append(nextValue)
        nextValue = x[len(x)-1] + x[len(x)-2]
    return x

# returns the sum of all even numbers in a list.
def addAllEvensInList(a):
    x = 0
    for i in a:
        if i%2 == 0:
            x += i
    return x

# solves for the answer
fibs = getFibonacciNumbers()
answer = addAllEvensInList(fibs)
print answer
