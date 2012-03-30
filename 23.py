import math

# returns the list of all the factors of the specified number
def factors(a):
    x = []
    for i in range(1,int(math.floor(math.sqrt(a)))+1):
        if a%i == 0:
            x.append(i)
            if a/i != i and a/i != a:
                x.append(a/i)
    x.sort()
    return x

# returns a list of all abundant numbers up to the specified number
def abundants(num):
    abundant = []
    for i in range(1,num+1):
        if sum(factors(i)) > i:
            abundant.append(i)
    return abundant
    
# returns a boolean list where each item tells whether its index is a
#   sum of two abundant numbers.
def whichAreSums(num,abundants):
    every = []
    for i in range(0,num+1):
        every.append(False)
    for i in range(0,len(abundants)):
        for j in range(0,i+1):
            s = abundants[i] + abundants[j]
            if s <= num:
                every[s] = True
    return every

# solves for the answer.
abundants = abundants(28123)
booleanList = whichAreSums(28123,abundants)
answer = 0
for a in range(0,28124):
    if not booleanList[a]:
        answer += a
print answer
