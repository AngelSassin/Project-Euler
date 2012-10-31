import functions

phis = functions.phiSieve(1000000)

# solves for the answer
total = long(0)
for i in phis:
    total += long(i)
print total-1 # because d cannot equal 1 if n is smaller than it and positive
