import random

spaces = [0]*40
players = [0]*4
chestCards = [1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
chanceCards = [1,2,3,4,5,6,7,8,9,10,0,0,0,0,0,0]
doubles = [0]*len(players)


def roll(player, sided):
    a = random.randint(1,sided)
    b = random.randint(1,sided)

    if a == b:
        doubles[player] += 1
    else:
        doubles[player] = 0

    return a+b

def chance(player):
    card = chanceCards.pop(0)
    chanceCards.append(card)

    if card == 1:
        players[player] = 0
    if card == 2:
        players[player] = 10
    if card == 3:
        players[player] = 11
    if card == 4:
        players[player] = 24
    if card == 5:
        players[player] = 39
    if card == 6:
        players[player] = 5
    if card == 7 or card == 8:
        if players[player] < 5 or players[player] >= 35:
            players[player] = 5
        elif players[player] < 15:
            players[player] = 15
        elif players[player] < 25:
            players[player] = 25
        else:
            players[player] = 35
    if card == 9:
        if players[player] < 12 or players[player] >= 28:
            players[player] = 12
        else:
            players[player] = 28
        players[player] = 0
    if card == 10:
        players[player] += 37
        players[player] %= 40

    return

def chest(player):
    card = chestCards.pop(0)
    chestCards.append(card)

    if card == 1:
        players[player] = 0
    if card == 2:
        players[player] = 10

    
    return

def shuffle():
    random.shuffle(chestCards)
    random.shuffle(chanceCards)

def takeTurn(player, sided):
    num = roll(player, sided)
    players[player] += num
    players[player] %= 40

    if doubles[player] == 3:
        players[player] = 10
        spaces[10] += 1
        doubles[player] = 0
        return

    #Space specific
    if players[player] == 30:
        players[player] = 10
    if players[player] == 2 or players[player] == 17 or players[player] == 33:
        chest(player)
    if players[player] == 7 or players[player] == 22 or players[player] == 36:
        chance(player)

    spaces[players[player]] += 1
    return

def findModal(num):
    maxes = ["00"]*num
    for num in range(len(maxes)):
        best = 0
        iBest = 30
        for i in range(len(spaces)):
            if spaces[i] > best:
                iBest = i
                best = spaces[i]
        maxes[num] = str(iBest)
        spaces[iBest] = 0
    return maxes



shuffle()
for turn in range(50000):
    for p in range(len(players)):
        takeTurn(p, 6)
modal = findModal(3)
print(str(modal[0]) + str(modal[1]) + str(modal[2]))
