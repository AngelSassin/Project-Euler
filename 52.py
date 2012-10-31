# returns a sorted list of the digits in a number
def digits(number):
    d = []
    while number:
        d.append(number%10)
        number /= 10
    d.sort()
    return d

# returns True if 2x, 3x, 4x, 5x, and 6x the number all contain the same digits.
def works(number):
    dig2 = digits(2*number)
    dig3 = digits(3*number)
    dig4 = digits(4*number)
    dig5 = digits(5*number)
    dig6 = digits(6*number)
    if dig2 == dig3 and dig3 == dig4 and dig4 == dig5 and dig5 == dig6:
        return True
    return False

# solves for the answer
answer = 0
i = 1
while answer == 0:
    if works(i):
        answer = i
        break
    i += 1
print answer
