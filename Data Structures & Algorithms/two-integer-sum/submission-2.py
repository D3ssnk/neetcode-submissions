class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index,number in enumerate(nums):
            needed = target - number
            if needed not in seen:
                seen[number] = index
            else:
                return [seen[needed], index] 


        