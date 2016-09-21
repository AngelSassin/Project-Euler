# Problem 80 #

import math
from decimal import *

def sum_digits(n):
    s = 0
    for x in n:
        if x != ".":
            s += int(x)
    return s

answer = 0
getcontext().prec = 110
for n in range(2, 100):
    if n not in [4, 9, 16, 25, 36, 49, 64, 81]:
        x = str(Decimal(n).sqrt())[:101]
        answer += sum_digits(x)
print(answer)
