# Time: O(nlogn)
# Space: O(num uniques)
def arrange(chars, min_sep):
    heap = []
    for char, count in Counter(chars).items():
        heappush(heap, (-1 * count, char))
    out = []
    while len(heap):
        elms = []
        for _ in range(min_sep):
            if len(heap) == 0:
                break
            elms.append(heappop(heap))
        for count, char in elms:
            out.append(char)
            count+=1
            if count < 0:
                heappush(heap, (count, char))
    return "".join(out) 
