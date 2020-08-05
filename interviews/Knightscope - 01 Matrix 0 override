'''
Given an M x N matrix consiting of only 0 and 1, change all elements of row i and column j to 0 if cell (i,j) has value 0.

Input:
[ 1 1 0 1 1 ] r0, c2
[ 1 1 1 1 1 ]
[ 1 1 1 0 1 ] r2, c3
[ 1 1 1 1 1 ]
[ 0 1 1 1 1 ] r4, c0

Expected Output:
[ 0 0 0 0 0 ]
[ 0 1 0 0 1 ]
[ 0 0 0 0 0 ]
[ 0 1 0 0 1 ]
[ 0 0 0 0 0 ]

- Consider only original input 0s -> create an output arr

Solutions:
1. as soon as we see a 0, resolve row and col
   - linear scan -> DFS to set 0s
2. linear scan through the matrix, add i j of 0 to a set
    - after first pass, make another pass to set 0s 
    - edge cases:
      - stop early if row is 0
'''

# Runtime: O(m*n)
# Space: O(m*n + max(m, n))
def matrixOverride(matrix):

    if not len(matrix):
        return -1

    m, n = len(matrix), len(matrix[0])
    output = [ [1 for _ in range(n)] for _ in range(m) ]
    zeroRow, zeroCol = set(), set()

    # first pass to detect 0s
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                zeroRow.add(i)
                zeroCol.add(j)
                break

    # second pass to set 0s
    for i in range(m):

        # if the row is marked as 0, override
        if i in zeroRow:
            output[i] = [0]*n
            continue

        # row is not marked, check each col
        for j in range(n):
            if j in zeroCol:
                output[i][j] = 0
    
    return output

# Testing
caseInput = [
    [ 1, 1, 0, 1, 1 ],
    [ 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 0, 1 ],
    [ 1, 1, 1, 1, 1 ],
    [ 0, 1, 1, 1, 1 ]
]
caseOutput = [
    [0, 0, 0, 0, 0], 
    [0, 1, 0, 0, 1], 
    [0, 0, 0, 0, 0], 
    [0, 1, 0, 0, 1], 
    [0, 0, 0, 0, 0]
]

print('Test 1')
print('output {}'.format(matrixOverride(caseInput)))
print('expected {}'.format(caseOutput))
