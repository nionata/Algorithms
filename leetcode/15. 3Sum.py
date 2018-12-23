class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        solutions, size = [], len(nums)
        nums.sort()
        for i in range(size):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = nums[i] * -1
            a, b = i + 1, size - 1
            while a < b:
                if nums[a] + nums[b] == target:
                    solutions.append([nums[a], nums[b], nums[i]])
                    a = a + 1
                    while a < b and nums[a] == nums[a - 1]:
                        a = a + 1
                elif nums[a] + nums[b] < target:
                    a = a + 1
                else:
                    b = b - 1
        return solutions
