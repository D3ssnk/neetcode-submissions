class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_seen = {}

        for i,n in enumerate(nums):
            r = target - n
            if r in nums_seen: return [nums_seen[r],i]
            else: nums_seen[n] = i
        

        