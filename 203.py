import prime

# returns Pascal's triangle to n rows
def pascalsTriangle(n):
    pascal = [[1]]*n
    for i in xrange(len(pascal)):
        pascal[i] = pascal[i]*(i+1)
        if i != 0:
            for j in xrange(len(pascal[i])):
                if j == 0 or j == i:
                    pascal[i][j] = 1
                else:
                    pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
    return pascal

def uniqueNumbers2DArray(array):
    numbers = set()
    for i in array:
        for j in i:
            numbers = numbers.union(set([j]))
    return numbers

numbers = uniqueNumbers2DArray(pascalsTriangle(51))

def isSquareFree(n):
    factors = prime.primeFactors(n)
    return len(factors) == len(set(factors))

def sumOfSquareFree(numberSet):
    total = 0
    for i in numberSet:
        if isSquareFree(i):
            total += i
    return total

# solves for the answer
print sumOfSquareFree(numbers)
