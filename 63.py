# solves for the answer
count = 0
power = 1
while power <= 21:
    num = 1
    while len(str(num**power)) != power:
        num += 1
    while len(str(num**power)) == power:
        num += 1
        count += 1
    power += 1
print count

# But why is there no n-digit number that is a n-power where n > 21?
