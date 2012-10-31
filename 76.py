answers = [[-1]*501 for x in xrange(501)]

def expand(min, sum):
	if answers[min][sum] != -1:
		return answers[min][sum]
	if min > sum:
		answers[min][sum] = 0
		return 0
	totals = 1
	for i in xrange((sum-min)/2 + 1):
		totals += expand(min + i, sum - (min + i))
	answers[min][sum] = totals
	return totals

# solves for the answer
print expand(1,100)
