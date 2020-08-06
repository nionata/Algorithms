class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        myDic = dict()
        for i, v in enumerate(nums):
            if target - v in myDic: return (i, myDic[target - v])
            myDic[v] = i
        
