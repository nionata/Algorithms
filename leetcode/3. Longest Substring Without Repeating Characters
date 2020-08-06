class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxSubStr, i, j = 0, 0, 0
        while j < len(s):
            subStr = s[i:j+1]
            uniqueSubStr = set(subStr)
            
            if len(uniqueSubStr) == len(subStr): 
                maxSubStr = max(len(subStr), maxSubStr)
                j += 1
            else:
                i +=1
        return maxSubStr
