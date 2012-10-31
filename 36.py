# returns the specified decimal number into a binary representation.
def binary(number):
    if number <= 1:
        return number
    base2 = 0
    i = 0
    while 2**(i+1) <= number:
        i += 1
    base2 += 10**i + binary(number-2**i)
    return base2

# returns True if the specified number is a palindrome
def isPalindrome(number):
    number = str(number)
    for i in range(0,(len(number)+1)/2):
        if number[i] != number[(len(number)-1)-i]:
            return False
    return True

# returns a list of all numbers which are palindromic in base 2 and 10
def bothPalindromic(belowThis):
    x = []
    for i in range(0,belowThis):
        if isPalindrome(i) and isPalindrome(binary(i)):
            x.append(i)
    return x

# solves for the answer
answer = bothPalindromic(1000000)
print sum(answer)
