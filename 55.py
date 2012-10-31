import string

# returns True if the number is a palindrome
def palindrome(number):
    word = str(number)
    backward = ''
    for i in range(len(word)-1,-1,-1):
        backward += word[i]
    if word == backward:
            return True
    return False

# returns True if the specified number is a Lychrel number
def isLychrel(number):
    for x in range(0,50):
        backward = ''
        for i in range(len(str(number))-1,-1,-1):
            backward += str(number)[i]
        number += int(backward)
        if palindrome(number):
            return False
    return True

# solves for the answer
answer = 0
for i in range(0,10000):
    if isLychrel(i):
        answer += 1
print answer
