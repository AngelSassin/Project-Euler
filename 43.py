'''
Analysis:
    1. For d4d5d6 to be divisible by 5, d6 must be 0 or 5.
    2. If d6 is 0, d7 must equal d8 for d6d7d8 to be divisible by 11.
        Since this is not possible, d6 must equal 5, and so we know
        that d6d7d8 is {506, 517, 528, 539, 561, 572, 583, 594}.
    3. Because d7d8d9 is divisible by 13, it reasons that d6d7d8d9
        is {5286, 5390, 5728, 5832}.
    4. Because d8d9d10 is divisible by 17, it reasons that d6d7d8d9d10
        is {52867, 53901, 57289}.
    5. Because d5d6d7 is dibisible by 7, the only two possibilities
        for d5d6d7d8d9d10 are 952867 and 357289.
    6. With the clue that d3d4d5 is divisible by 3, it reasons that
        d3d4d5d6d7d8d9d10 is {03952867, 30952867, 06357289, 60357289}.
    7. Since d2d3d4 is divisible by 2, d4 is even, and so
        d3d4d5d6d7d8d9d10 is {30952867, 06357289, 60357289}.
    8. With no other clues, we are left with the following combinations:
            for d5d6d7d8d9d10 = 952867:
                d1d2d3d4 is {1430, 4130}.
            for d5d6d7d8d9d10 = 357289:
                d1d2d3d4 is {1406, 4106, 1460, 4160}.

So, there are 6 pandigital numbers with this property.
There's no need for programming. We will just sum these numbers.   
'''

# 'solves' for the answer
answer = ((1430+4130+1406+4106+1460+4160)*(10**6))+2*952867+4*357289
print answer
