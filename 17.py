# the terms to use for the numbers
terms = ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
tenTerms = ['Zero','Ten','Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']

# returns a written-out description of a specified number up to 9999
def getDescription(number):
    ones = (number/1)%10
    tens = (number/10)%10
    hundreds = (number/100)%10
    thousands = (number/1000)%10
    description = ''
    if thousands > 0:
        description += terms[thousands] + 'Thousand'
    if hundreds > 0:
        description += terms[hundreds] + 'Hundred'
    if number > 100 and (tens > 0 or ones > 0):
        description += 'And'
    if tens == 1:
        description += terms[(tens*10)+ones]
    else:
        if tens > 0:
            description += tenTerms[tens]
        if ones > 0:
            description += terms[ones]
    return description

# solves for the answer
answer = 0
for i in range(0,1000):
    answer += len(getDescription(i+1))
print answer
