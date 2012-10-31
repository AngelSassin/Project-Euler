# returns the nth digit of the fractional part
def d(n):
    fractionalPart = '.'
    number = 1
    while len(fractionalPart) <= n:
        fractionalPart += str(number)
        number += 1
    return int(fractionalPart[n])

# solves for the answer
answer = 1
for i in range(0,7):
    answer *= d(10**i)
print answer
