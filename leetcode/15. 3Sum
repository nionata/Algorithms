class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n, sol = len(nums)-1, []
        
        for i in range(n-1):
            l, r = i + 1, n
            
            while l < r:
                currSum = nums[i] + nums[l] + nums[r]
                
                if currSum == 0 and (i == 0 or nums[i] != nums[i - 1]):
                    sol.append([nums[idx] for idx in [l, r, i]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                        continue
                elif currSum < 0:
                    l += 1
                else:
                    r -= 1
                
        return sol
