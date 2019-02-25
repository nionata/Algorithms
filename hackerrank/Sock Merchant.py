def sockMerchant(n, ar):
    ar.sort()
    stack, pairs = [], 0
    for i in range(n):
        num = ar[i]
        if stack and num == stack[-1]:
            pairs += 1
            stack.pop()
        else:
            stack.append(num)
    return pairs
