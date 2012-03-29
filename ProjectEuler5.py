# returns the greatest common divisor of the two specified numbers.
def gcd(a,b):
    if a%b == 0:
        return b
    else:
        return gcd(b,a%b)

# returns the least common multiple of the two specified numbers.
def lcm(a,b):
    return (a*b)/gcd(a,b)

# returns the least common multiple of all the numbers in a list.
def lcmList(x):
    multiple = 1
    for i in x:
        multiple = lcm(multiple,i)
    return multiple

# solves for the answer
list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
answer = lcmList(list)
print answer
