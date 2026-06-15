class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_height = 0
        while l < r:
            value = min(heights[l],heights[r]) * (r-l)
            max_height = max(value, max_height)
            if heights[l] < heights[r]: l+=1
            elif heights[l] > heights[r]: r-=1
            else: l += 1
        return max_height
        