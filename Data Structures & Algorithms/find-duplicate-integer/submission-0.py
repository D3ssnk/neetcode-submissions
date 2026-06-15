class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen_numbers = set()
        for number in nums:
            if number in seen_numbers: return number
            seen_numbers.add(number)
        