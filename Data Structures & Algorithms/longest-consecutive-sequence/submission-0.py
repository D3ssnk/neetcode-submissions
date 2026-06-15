class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums_set = set(nums)
        for number in nums:
            tracker = number
            temp_long = 0
            if tracker in nums_set:
                tracker -= 1
                temp_long += 1
                while tracker in nums_set:
                    temp_long += 1
                    tracker -= 1
            longest = max(longest,temp_long)
        
        return longest
            
        