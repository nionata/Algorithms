'''
support open (<x>) and close (</x>)
<strong>foo</strong>

Ignore pain text 
Care: < > / 

<strong>foo</strong>

Parse an individual tag - One off, no mem
Parse the whole input - Stack


<strong>foo</strong>

Scan through looking for < 
  - if another < -> False
  - if >, add tag to stack

if self-closing, don't add to stack - / look-ahead

Check the len of stack 

Improvements:
1. Move tag parser to a seperate function
2. Parse the whole tag in-between < and > first
3. Break down the parsed tag to get the variables and booleans

'''

# Runtime: O(n) / Space: O(n)
def parseXml(xml):
    stack, i = [], 0
    while i < len(xml):
        if xml[i] == "<":
            closing, j = False, i+1
            if j < len(xml) and xml[j] == "/":
                closing, j = True, j+1
            while j < len(xml):
                # add to handle selfclose
                c = xml[j]
                print('c', c)
                if c == "<":
                    return False
                elif c == ">":
                    if closing:
                        if xml[i+2:j] != stack.pop():
                            return False
                    else:
                        stack.append(xml[i+1:j])
                    break
                j+=1
            i = j
        i+=1
        return len(stack) == 0

cases = [
    ("<strong>foo</strong>", True),
    ("<foo><bar></bar></foo>", True),
    ("<foo><bar></bar>", False)
]

for i, expected in cases:
    print(i, parseXml(i), expected)
