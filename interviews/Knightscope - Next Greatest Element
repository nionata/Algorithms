'''
Given an array, return an array with the next greatest element. If no greater element, use -1

input: [3, 16, 4, 16, 20, 23]
expected output: [16, 20, 16, 20, 23, -1]

input: [1, 2, 3, 4, 7, 8, 9]
expected output: [2, 3, 4, 7, 8, 9, -1]

input: [1, 10, 3, 4, 7, 8, 9]
expected output: [10, -1, 4, 7, 8, 9, -1]

- Don't want to just look next
- Need to resolve not next greatest
- Interatively

Solutions
1. brute force - o(n^2)
2. single pass w/ stack - o(n)

- Need a DS that can store unresolved numbers
- Stack store each element
- Visit an element, check the stack to see if we can resolve previous numbers
- Resolved the other numbers, flush the stack by setting all unresolved numbers to -1
'''

# Runtime: O(n)
# Space: O(n)
def nextGreatest(numbers):

    stack = []

    for i, num in enumerate(numbers):
        while stack and stack[-1][1] < num:
            unresolved_idx, unresolved_number = stack.pop()
            numbers[unresolved_idx] = num

        stack.append((i, num))

    while stack: 
        unresolved_idx, unresolved_number = stack.pop()
        numbers[unresolved_idx] = -1

# Testing 
testCases = [
    ([3, 16, 4, 16, 20, 23], [16, 20, 16, 20, 23, -1]),
    ([1, 2, 3, 4, 7, 8, 9], [2, 3, 4, 7, 8, 9, -1]),
    ([1, 10, 3, 4, 7, 8, 9], [10, -1, 4, 7, 8, 9, -1])
]

for i, case in enumerate(testCases):
    inputArr, outputArr = case
    nextGreatest(inputArr)

    print('Test {}'.format(i+1))
    print('ouput {}'.format(inputArr))
    print('expected {}'.format(outputArr))

    if i != len(testCases)-1:
        print('')
