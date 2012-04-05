day = 1 # 0 = Sunday, 1 = Monday, etc
year = 1900
month = 1
totalSunday = 0
while year <= 2000:
    #print str(month) + ', ' + str(year)
    if year != 1900:
        if day%7 == 0:
            totalSunday += 1
    if month == 2:
        if year%4 == 0:
            day += 29
        else:
            day += 28
    elif month == 4 or month == 6 or month == 9 or month == 11:
        day += 30
    else:
        day += 31
    if month == 12:
        year += 1
    month = (month%12)+1
print totalSunday
