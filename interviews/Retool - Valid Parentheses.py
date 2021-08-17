'''
()
{}
[]
(){}[]
((){}[])
([{}])

Improvements:
- Runtime/config value
- More dynamic passed in pairs
'''

pairs = {
    "(": ")",
    "{": "}",
    "[": "]"
}

# Runtime: O(n) / Space: O(n)
def parse(brackets):
    stack = []
    for c in brackets:
        if c in pairs:
            stack.append(c)
            continue
        if not len(stack):
            return False
        r_pair = pairs[stack.pop()]
        if r_pair != c:
            return False
    if len(stack) > 0:
        return False
    return True

cases = [
    ("([{}])", True),
    ("()", True),
    ("[]", True),
    ("{}", True),
    ("", True),
    ("{([)]}", False),
    ("({)}", False),
    ("{", False)
]

for i, expected in cases:
    print(i, parse(i), expected)