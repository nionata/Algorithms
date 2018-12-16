class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        myDick = dict()
        for i, v in enumerate(nums):
            if target - v in myDick: return (i, myDick[target - v])
            myDick[v] = i
        
