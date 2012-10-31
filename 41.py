import math

# returns the n'th lexicographic permutation of a string.
def getPermutation(n, string):
    n -= 1
    a = []
    for i in string:
        a.append(i)
    end = ''
    for i in range(0,len(string)):
        size = len(a)
        perm = math.factorial(size)
        addition = a[n/(perm/size)]
        end += addition
        a.remove(addition)
        n %= perm/size
    return end

# returns True if the specified number is prime
def isPrime(a):
    if a <= 1:
        return False
    for i in range(2,int(math.floor(math.sqrt(a)))+1):
        if a%i == 0:
            return False
    return True

# returns True if the specified number is pandigital
def isPandigital(number):
    digits = []
    while number:
        digits.append(number%10)
        number /= 10
    digits.sort()
    if digits == range(1,len(digits)+1):
        return True
    return False

# solves for the answer
n = 0
answer = 0
while answer == 0:
    pandigital = int(getPermutation(n,'7654321'))
    if isPrime(pandigital):
        answer = pandigital
    n += 1
print answer
