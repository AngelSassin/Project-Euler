import string

# makes the hands
def makeHands():
    file = open('poker.txt','r')
    hands = file.read().split('\n')
    for i in hands:
        h = i.split(' ')
        hand1.append((h[0],h[1],h[2],h[3],h[4]))
        hand2.append((h[5],h[6],h[7],h[8],h[9]))

# the hands
hand1 = []
hand2 = []
makeHands()

# returns the value of the rank
def v(c):
    if c == 'T':
        return 10
    if c == 'J':
        return 11
    if c == 'Q':
        return 12
    if c == 'K':
        return 13
    if c == 'A':
        return 14
    return int(c)

# returns True if the hand is a Flush
def isFlush(h):
    if h[0][1] == h[1][1] == h[2][1] == h[3][1] == h[4][1]:
        return True
    return False

# returns the value of the rank if the hand has at least one pair
def hasOnePair(h):
    cards = [h[0][0],h[1][0],h[2][0],h[3][0],h[4][0]]
    cards.sort()
    count = 0
    prev = 0
    for i in cards:
        if i == prev:
            count += 1
        elif count == 2:
            return prev
        else:
            count = 1
        prev = i
    if count == 2:
        return prev
    return False

# returns the two values, higher value first, of the ranks if the hand is
#   a Two Pair
def isTwoPair(h):
    cards = [h[0][0],h[1][0],h[2][0],h[3][0],h[4][0]]
    cards.sort()
    pairs = 0
    ranks = []
    count = 0
    prev = 0
    for i in cards:
        if i == prev:
            count += 1
        elif count == 2:
            pairs += 1
            ranks.append(prev)
            count = 1
        else:
            count = 1
        prev = i
    if (count == 2 and pairs == 1):
        ranks.append(prev)
        if v(ranks[0]) > v(ranks[1]):
            return ranks[0] + ranks[1]
        return ranks[1] + ranks[0]
    elif pairs == 2:
        if v(ranks[0]) > v(ranks[1]):
            return ranks[0] + ranks[1]
        return ranks[1] + ranks[0]
    return False

# returns the value of the rank if the hand is a Three Of A Kind
def isThreeKind(h):
    cards = [h[0][0],h[1][0],h[2][0],h[3][0],h[4][0]]
    cards.sort()
    rank = 0
    count = 0
    prev = 0
    for i in cards:
        if i == prev:
            count += 1
        elif count == 3:
            return prev
        else:
            count = 1
        prev = i
    if count == 3:
        return prev
    return False

# returns the value of the rank if the hand is a Four Of A Kind
def isFourKind(h):
    cards = [h[0][0],h[1][0],h[2][0],h[3][0],h[4][0]]
    cards.sort()
    rank = 0
    count = 0
    prev = 0
    for i in cards:
        if i == prev:
            count += 1
        elif count == 4:
            return prev
        else:
            count = 1
        prev = i
    if count == 4:
        return prev
    return False

# returns the value of the Three Of A Kind if the hand is a Full House
def isFullHouse(h):
    if hasOnePair(h):
        return isThreeKind(h)

# returns the lowest value of the Straight if the hand is a Straight
def isStraight(h):
    cards = [v(h[0][0]),v(h[1][0]),v(h[2][0]),v(h[3][0]),v(h[4][0])]
    cards.sort()
    prev = cards[0]
    for i in cards[1:5]:
        if i != prev + 1:
            return False
        prev = i
    return str(cards[0])

# returns True if the hand is a Royal Flush
def isRoyalFlush(h):
    if isFlush(h):
        cards = [h[0][0],h[1][0],h[2][0],h[3][0],h[4][0]]
        rFl = ['T','J','Q','K','A']
        rFl.sort()
        cards.sort()
        if cards == rFl:
            return True
    return False

# returns the lowest value of the Straight if the hand is a Straight Flush
def isStraightFlush(h):
    if isFlush(h):
        return isStraight(h)

# returns a representation of the hand from highest card to lowest card
def highCard(h):
    c = [v(h[0][0]),v(h[1][0]),v(h[2][0]),v(h[3][0]),v(h[4][0])]
    c.sort()
    for i in range(0,5):
        if c[i] == 10:
            c[i] = 'T'
        if c[i] == 11:
            c[i] = 'J'
        if c[i] == 12:
            c[i] = 'Q'
        if c[i] == 13:
            c[i] = 'K'
        if c[i] == 14:
            c[i] = 'A'
        c[i] = str(c[i])
    return c[4]+c[3]+c[2]+c[1]+c[0]

# returns the score of the hand:
#   '3Q' 3-of-a-kind queens
#   '85' means straight-flush, 5 is lowest
#   ....etc.
def score(hand):
    theScore = ''
    if isRoyalFlush(hand):
        theScore += '9'
    elif isStraightFlush(hand):
        theScore += '8' + isStraightFlush(hand)
    elif isFourKind(hand):
        theScore += '7' + isFourKind(hand)
    elif isFullHouse(hand):
        theScore += '6' + isFullHouse(hand)
    elif isFlush(hand):
        theScore += '5'
    elif isStraight(hand):
        theScore += '4' + isStraight(hand)
    elif isThreeKind(hand):
        theScore += '3' + isThreeKind(hand)
    elif isTwoPair(hand):
        theScore += '2' + isTwoPair(hand)
    elif hasOnePair(hand):
        theScore += '1' + hasOnePair(hand)
    else:
        theScore += '0'
    return theScore + highCard(hand)

# returns 1 if player 1 wins, 2 if player 2 wins, or False if there's no winner.
def winner(h1,h2):
    s1 = score(h1)
    s2 = score(h2)
    for x in range(0,len(s1)):
        if v(s1[x]) > v(s2[x]):
            return 1
        if v(s1[x]) < v(s2[x]):
            return 2
    return False

# solves for the answer
answer = []
for i in range(0,len(hand1)):
    if winner(hand1[i],hand2[i]) == 1:
        answer.append(score(hand1[i]) + ' | ' + score(hand2[i]))
print len(answer)
