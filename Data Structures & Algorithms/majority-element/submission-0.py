class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_seen = defaultdict(int)

        for number in nums:
            nums_seen[number] += 1
            if nums_seen[number] > len(nums) / 2:
                return number
        

        