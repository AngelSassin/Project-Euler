import string
import math

# the words
file = open('words.txt','r')
words = file.read().split(',')

# returns the list of all the factors of the specified number
def factors(a):
    x = []
    for i in range(1,int(math.floor(math.sqrt(a)))+1):
        if a%i == 0:
            x.append(i)
            if (a/i != i):
                x.append(a/i)
    x.sort()
    return x

# returns the value of the word
def wordValue(word):
    value = 0
    for char in word:
        value += string.ascii_uppercase.find(char)+1
    return value

# returns True if the specified word is a triangle word
def isTriangleWord(word):
    value = wordValue(word)
    value *= 2
    for factor in factors(value):
        if value/factor == factor+1 or value/factor == factor-1:
            return True
    return False

# solves for the answer
answer = 0
for word in words:
    if isTriangleWord(word):
        answer += 1
print answer
    
