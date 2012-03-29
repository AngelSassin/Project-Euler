# tests whether the specified number is a palindrome.
def isPalindrome(num):
    original = num
    reverse = 0
    while (num > 0): #
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num / 10
    return original == reverse
        
# returns the list of all palindromes made from products of two 3-digit numbers.
def getPalindromeList():
    x = []
    for i in range(0,900):
        for j in range(0,i):
            product = (999-i)*(999-j)
            if isPalindrome(product):
                x.append(product)
    return x

# solves for the answer.
palindromes = getPalindromeList()
palindromes.sort()
answer = palindromes[len(palindromes)-1]
print answer
