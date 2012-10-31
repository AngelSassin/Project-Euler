import clock

# the worths of each coin cooresponding to the list indeces
worth = [1,2,5,10,20,50,100,200]

# returns the total amount of money in the specified combination of coins
def sumMoney(money):
    sum = 0
    for i in range(0,8):
        sum += money[i]*worth[i]
    return sum

# returns all the possible coin combinations to make 200 pence
def getCombinations(theMoney):
    combination = [0,0,0,0,0,0,0,0]
    total = []
    while combination[0] != theMoney:
        index = 1
        while combination[index] == 0 and index < 7:
            index += 1
        if len(total) != 0:
            combination[index] -= 1
            index -= 1
        for i in range(0,index+1):
            combination[i] = 0
        money = sumMoney(combination)
        while money != theMoney:
            combination[index] += (theMoney-money)/worth[index]
            index -= 1
            money = sumMoney(combination)
        total.append(combination[:])
    return total

# solves for the answer
print len(getCombinations(200))
