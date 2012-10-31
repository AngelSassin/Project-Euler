# returns the answer 
def everything():
    total = 0
    for i in range(1,1001):
        total += i**i
    total = str(total)
    return str(total)[len(str(total))-10:len(str(total))]

# solves for the answer
answer = everything()
print answer
