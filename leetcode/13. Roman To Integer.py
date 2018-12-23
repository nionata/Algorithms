class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        symbols = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sum = 0
        for i in range(len(s)):
            char = s[i]
            if (char == 'I' or char == 'X' or char == 'C') and i+1 != len(s):
                nextChar = s[i+1]
                if symbols[char] < symbols[nextChar]:
                    sum -= symbols[char]
                    continue
            sum += symbols[char]
        return sum
