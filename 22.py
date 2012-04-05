import string

# the names
file = open('names.txt','r')
names = file.read().split(',')

# returns the worth of a name
def worth(name):
    letters = '"' + string.ascii_uppercase
    worth = 0
    for i in range(0,len(name)):
        worth += letters.index(name[i])
    return worth

# returns the list of the scores of the names
def score(nameList):
    nameList.sort()
    scores = []
    for i in range(0,len(nameList)):
        scores.append((i+1)*worth(nameList[i]))
    return scores

# solves for the answer
scoreList = score(names)
answer = sum(scoreList)
print answer
