import string

# the cipher
cipher = open('cipher1.txt','r')
cipher = cipher.read().split(',')
for i in range(0,len(cipher)):
    cipher[i] = int(cipher[i])

# returns the decripted list of ascii codes using the specified encription key
def decript(theKey):
    key = []
    for i in theKey:
        key.append(ord(i))
    decripted = []
    for d in range(0,len(cipher[:])):
        decripted.append(int(cipher[d])^key[d%len(key)])
    return decripted

# returns a list of characters represented by the specified ascii codes
def toChars(theList):
    chars = []
    for i in theList:
        chars.append(chr(i))
    return chars

# returns the ascii string for the specified ascii codes
def asciiString(theList):
    theString = ''
    for code in theList:
        theString += chr(code)
    return theString

# returns the possible encription keys
def findKey():
    possible = []
    keyChars = string.ascii_lowercase
    fail = [False]*3
    for a in keyChars:
        fail[0] = False
        for b in keyChars:
            fail[1] = False
            for c in keyChars:
                temp = a+b+c
                theTest = test(temp)
                if theTest == 3:
                    possible.append(temp[:])
                else:
                    fail[theTest] == True
                if fail[0] or fail[1]:
                    break
            if fail[0]:
                break
    return possible

# returns 3 if the specified key works, else returns the index of the key
#   that failed the test.
def test(theKey):
    illegal = range(0,32)
    illegal.extend(range(127,256))
    uppers = string.ascii_uppercase
    lowers = string.ascii_lowercase
    numbers = string.digits
    endPunct = '.?!'
    startPunct = '"('''
    firstCharacter = chr(cipher[0]^ord(theKey[0]))
    if not firstCharacter in startPunct+string.ascii_uppercase:
        return 0
    lastCharacter = chr(cipher[len(cipher)-1]^ord(theKey[(len(cipher)-1)%3]))
    if not lastCharacter in endPunct:
        return (len(cipher)-1)%3
    final = decript(theKey)
    finalAscii = asciiString(final)
    if finalAscii[0] == '(':
        if not ')' in finalAscii:
            return 2
    if len(set(final) & set(illegal)) > 0:
        return finalAscii.find(chr(list((set(final) & set(illegal)))[0]))%3
    if finalAscii.count('"')%2 == 1:
        return finalAscii.find('"')%len(theKey)
    pTest = finalAscii[:]
    while pTest.count('.') > 1:
        periodIndex = pTest.find('.')
        while not pTest[periodIndex] in uppers+lowers:
            periodIndex += 1
        if pTest[periodIndex] in lowers:
            return periodIndex%3
        pTest = pTest[periodIndex:len(pTest)]
    qTest = finalAscii[:]
    while qTest.count('?') > 1:
        questionIndex = qTest.find('?')
        while not qTest[questionIndex] in uppers+lowers:
            questionIndex += 1
        if qTest[questionIndex] in lowers:
            return questionIndex%3
        qTest = qTest[questionIndex:len(qTest)]
    eTest = finalAscii[:]
    while eTest.count('!') > 1:
        exclamIndex = eTest.find('!')
        while not eTest[exclamIndex] in uppers+lowers:
            exclamIndex += 1
        if eTest[exclamIndex] in lowers:
            return exclamIndex%3
        eTest = eTest[exclamIndex:len(eTest)]
    numTest = finalAscii[:]
    while len(set(numTest)&set(numbers)) > 0:
        for num in numbers:
            numIndex = numTest.find(num)
            while numTest[numIndex] in numbers+'.,':
                numIndex += 1
            if numTest[numIndex] != ' ':
                return numIndex%3
            numTest = numTest[numIndex:len(numTest)]
    return 3

# solves for the answer
answer = 0
for c1 in range(ord('a'),ord('z')+1):
    for c2 in range(ord('a'),ord('z')+1):
        for c3 in range(ord('a'),ord('z')+1):
            result = test(chr(c1)+chr(c2)+chr(c3))
            if result == 3:
                answer = decript(chr(c1)+chr(c2)+chr(c3))
            if answer != 0:
                break
        if answer != 0:
            break
    if answer != 0:
        break
print sum(answer)

