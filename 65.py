# The form of 'e' is [2;1,2,1,1,4,1,1,6,1,...,1,2k,1,...].
# The convergents of 'e' are 2,3,8/3,11/4,19/7,87/32,106/39,193/71,1264/465...
# The constant 'e' can be written as 2+1/(1+1/(2+1/(1+1/(1+1/(4+1/(1+...))))))

# returns the tuple (numerator,denominator) of the infinite continued fraction
#   with the specified form at the specified iteration.
def asdf(form,it):
    assert form[0] == '[' and form[len(form)-1] == ']'
    start = form[1:len(form)-2].split(';')
    sequence = start[1].split(',')
    length = len(sequence)
    repeated = False
    if sequence[0][0] == '(':
        repeated = True
        sequence[0] = sequence[0][1:len(sequence[0])]
        if length > 1:
            sequence[length-1] = sequence[length-1][:len(sequence[length-1])-1]
    first = int(start[0])
    if it == 0:
        return (first,1)
    it -= 1
    if not repeated:
        it %= length
    numerator = 0
    denominator = 1
    while it >= 0:
        add = int(sequence[it%length])
        numerator += add*denominator
        temp = numerator
        numerator = denominator
        denominator = temp
        it -= 1
    numerator += first*denominator
    return (numerator,denominator)

# returns the form of a fraction with the specified repeated sequence
def makeForm(repeated,first,sequence):
    form = '[' + str(first) + ';'
    if repeated:
        form += '('
    for i in sequence:
        form += str(i) + ','
    form = form[0:len(form)-1]
    if repeated:
        form += ')'
    return form + ']'

seq = []
for i in range(1,40):
    seq.extend([1,i*2,1])
form = makeForm(False,2,seq)
iterations = []
for i in range(0,100):
    iterations.append(asdf(form,i))
last = iterations[len(iterations)-1][0]
answer = 0
while last:
    answer += last%10
    last /= 10
print answer
