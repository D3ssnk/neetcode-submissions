class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen_numbers = set()
        max_count = 0
        for number in nums:
            count = 0
            seen_numbers.add(number)
            num = number
            while num in seen_numbers:
                count += 1
                num -= 1
            num = number 
            while num+1 in seen_numbers:
                count += 1
                num += 1
            max_count = max(max_count, count)
        
        return max_count

        