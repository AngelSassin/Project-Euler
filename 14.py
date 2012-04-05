import time

# The Collatz Problem starts with an integer. In one iteration, if the
#   number is even, divide by 2. If it is odd, multiply by 3 and add 1.
#   The problem is whether every integer will always end with 1.

# returns the number, under the specified number, that produces the
#   longest chain in the Collatz Problem.
def tableCollatz(number):
    longest = 1
    attempts = []
    for a in range(0,number):
        attempts.append(0)
    for i in range(1,number):
        num = i
        iTerms = 0
        while num > 1:
            iTerms += 1
            if num%2 == 0:
                num /= 2
            else:
                num = (num*3)+1
            if num < len(attempts):
                if attempts[num] != 0:
                    iTerms += attempts[num]
                    break
        attempts[i] = iTerms
        if iTerms > attempts[longest]:
            longest = i
    return longest
    
# solves for the answer
answer = tableCollatz(1000000)
print answer
