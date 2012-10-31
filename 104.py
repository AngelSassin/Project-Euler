# tells whether the number is pandigital from 1 to 9.
def isPandigital(n):
    has = set()
    while n:
        has.add(n%10)
        n /= 10
    return len(has) == 9 and not 0 in has

def works1(f):
    f = str(f)
    y = int(f[:9])
    return isPandigital(y)

def works2(f):
    return isPandigital(f%1000000000)

# solves for the answer
f1 = 1
f2 = 1
answer = 2
while not works2(f2) or not works1(f2):
    f3 = f1+f2
    f1 = f2
    f2 = f3
    k += 1
print answer
