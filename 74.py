import math

# the chains for each index
chains = [0]*3000000

# the factorials
facts = []
for i in xrange(10):
    facts.append(math.factorial(i))

# the sum of the factorials
def sumFacts(num):
    digits = []
    while num:
        digits.append(num%10)
        num /= 10
    total = 0
    for i in digits:
        total += facts[i]
    return total

# inputs the number of non-repeated terms in a chain into the list of chains
def chain(num):
    seen = []
    while not num in seen and chains[num] == 0:
        seen.append(num)
        num = sumFacts(num)
    length = len(seen)
    length += chains[num]
    for i in xrange(len(seen)):
        if chains[seen[i]] == 0:
            chains[seen[i]] = length-i

# solves for the answer
for i in xrange(1000000):
    if chains[i] == 0:
        chain(i)
answer = 0
for i in chains:
    if i == 60:
        answer += 1
print answer
