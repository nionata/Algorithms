# O(n) / O(1)
class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        m, s = max(milestones), sum(milestones)
        spacers = s-m
        if spacers >= m:
            return s
        return (2*spacers)+1
