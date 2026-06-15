class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        needed_num = {}
        for i in range(len(nums)):
            rnum = target - nums[i]
            if rnum in needed_num: return [needed_num[rnum],i]
            else: needed_num[nums[i]] = i
    

        