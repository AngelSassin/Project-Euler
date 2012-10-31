import prime
import search

primes = prime.primesTo(500)
answers = [[-1]*501 for x in xrange(501)]

def expand(min, sum):
    if answers[min][sum] != -1:
        return answers[min][sum]
    if min > sum:
        answers[min][sum] = 0
        return 0
    if search.searchList(primes,sum):
        totals = 1
    else:
        totals = 0
    for i in xrange((sum-min)/2 + 1):
        if search.searchList(primes,min+i):
            totals += expand(min + i, sum - (min + i))
    answers[min][sum] = totals
    return totals

# solves for the answer
i = 0
temp = expand(2,i)
while temp < 5000:
    i += 1
    temp = expand(2,i)
print i
