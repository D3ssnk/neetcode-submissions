class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        minVal = float("inf")
        while l <= r:
            m = (l + r) // 2
            if nums[l] < nums[r]: minVal = min(nums[l], minVal);
            if nums[m] >= nums[l]: l = m + 1
            else: r = m - 1
            minVal = min(nums[m], minVal)
        return minVal  
        
        