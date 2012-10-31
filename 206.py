# returns the number made from inserting the specified digits into the form
def insert(string, digits):
    result = ''
    for i in range(0,len(string)):
        if i%2 == 0:
            result += string[i]
        else:
            result += str(digits[(i-1)/2])
    return int(result)

# returns the square with the specified form
def findSquareIn(string):
    numberInsert = [9]*8
    numberInsert.append(0)
    leng = len(numberInsert)
    test = insert(string,numberInsert)
    if test**.5%2 == 0:
        return test
    while numberInsert != [0]*leng:
        i = leng-2
        while numberInsert[i] == 0:
            i -= 1
        while i != leng-1:
            numberInsert[i] = (numberInsert[i]-1)%10
            i += 1
        test = insert(string,numberInsert)
        if test**.5%2 == 0:
            return test
    return None

# solves for the answer
answer = findSquareIn('1_2_3_4_5_6_7_8_9_0')
print int(answer**.5)
        
