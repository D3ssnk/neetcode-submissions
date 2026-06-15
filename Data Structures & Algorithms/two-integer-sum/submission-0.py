class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_number = {}
        for index, number in enumerate(nums):
            needed_number = target - number
            if needed_number not in seen_number:
                seen_number[number] = index
            else:
                return [seen_number[needed_number],index]

        