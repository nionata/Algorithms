'''
Input:
- random list of chars
- min seperation of unique chars

Goal:
- each char should follow min sep.

input list: A A A B B C
minimum separation: 2
example output: A B A B A C | A B C A B A

MIN, can be further apart

- First pass - counter and sort
{
    A: 3,
    B: 2,
    C: 1
}

ABCABA

A:4 B:2 C:1

Level playing field
Only drift right for min S

A B A B A C A

A B A B A C A

A:2 C:1 B:0

A B A B A B A

A:2 B:2 C:2 min: 2

A B A B C C

Level playing field
Only drift right for min S | till right pair is larger

A B C A B C

- Second pass
Loop through each char, append to str builder

Assume: only solvable inputs

- Heap to keep track of max counts
- Heap pop/push based on min distance

Space: O(num uniques)
Time: O(chars/min distance logn)


{
    A: 4,
    B: 2,
    C: 1
}
2

[(), (), ()]
A B A B A C A

'''

# Time: O(nlogn)
# Space: O(num uniques)
def arrange(chars, min_sep):
    counts, heap = Counter(chars), []
    for char, count in counts:
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
    return out.strings()