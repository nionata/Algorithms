class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pairs = {")": "(", "]": "[", "}": "{"}
        stack = []
        for char in s:
            if char in pairs:
                if len(stack) != 0 and stack[-1] == pairs[char]:
                    stack.pop()
                else:
                    return False
            else: 
                stack.append(char)
        return not stack
