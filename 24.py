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

# solves for the answer.
print getPermutation(1000000,'0123456789')
