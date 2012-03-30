# returns the first fibonacci term with the specified number of digits
def fibonacciWithDigits(digits):
    sequence = [1,1]
    term = 2
    while len(str(sequence[len(sequence)-1])) < 1000:
        sequence.append(sequence[len(sequence)-1]+sequence[len(sequence)-2])
        term += 1
    return term

# solves for the answer.
answer = fibonacciWithDigits(1000)
print answer
