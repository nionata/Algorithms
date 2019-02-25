def repeatedString(s, n):
    aCount, addCount, i, overflow = 0, 0, 0, n%len(s)
    for c in s:
        if c == 'a':
            aCount += 1
            if i < overflow: addCount += 1
        i+=1
    return int((aCount*((n-overflow)/len(s)))+addCount)
    
 def repeatedString(s, n):
    return (s.count('a')*(n//len(s)))+s[:n%len(s)].count('a')
