# the romans
file = open('roman.txt','r')
romans = file.read().split('\n')

def fix(roman):
    toFix = roman[:]
    fixTuples = [('IIIII','V'),('IIII','IV'),('VV','X'),('VIV','IX')]
    fixTuples.extend([('XXXXX','L'),('XXXX','XL'),('LL','C'),('LXL','XC')])
    fixTuples.extend([('CCCCC','D'),('CCCC','CD'),('DD','M'),('DCD','CM')])
    for i in fixTuples:
        while i[0] in toFix:
            toFix = toFix.replace(i[0],i[1])
    return toFix

# solves for the answer
original = ''
answer = ''
for r in romans:
    original += r
    answer += fix(r)
print original
print answer
print len(original)
print len(answer)
print len(original) - len(answer)
