def stringDigits(num):
    digits = []
    while num:
        digits.append(str(num%10))
        num /= 10
    digits.sort()
    return digits

def cubesTo(high):
    theCubes = []
    i = 1
    while i**3 < high:
        theCubes.append(i**3)
        i += 1
    return theCubes

# the cubes
L = 900000000000
cubes = cubesTo(L)
cubeDigits = [0]*len(cubes)

# solves for the answer
for i in xrange(len(cubes)):
    cubeDigits[i] = stringDigits(cubes[i])
sortedCubes = cubeDigits[:]
sortedCubes.sort()

this = []
count = 1
for cube in sortedCubes:
    if cube == this:
        count += 1
    else:
        count = 1
        this = cube
    if count == 5:
        break
for i in xrange(len(cubeDigits)):
    if cubeDigits[i] == this:
        print cubes[i]
        break
