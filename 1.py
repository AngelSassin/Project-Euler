# returns the list of all multiples of 3 and 5 below 1000.
def getMultiplesOf3and5():
    x = []
    for i in range (0,1000):
        if i%3 == 0 or i%5 == 0:
            x.append(i)
    return x

# returns the sum of all the elements in the specified list.
def addAllElementsInList(a):
    x = 0
    for i in a:
        x += i
    return x

# solves for the answer
list = getMultiplesOf3and5()
answer = addAllElementsInList(list)
print answer
