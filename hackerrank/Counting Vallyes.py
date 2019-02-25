def countingValleys(n, s):
    vallies, elevation = 0, 0
    for i in range(n):
        change = s[i]
        if change == "D":
            elevation -= 1
        else:
            elevation += 1
            if elevation == 0: vallies += 1
    return vallies
