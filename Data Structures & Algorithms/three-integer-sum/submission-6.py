class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        seen = set()
        answer = []
        for index, number in enumerate(nums):
            l = index + 1
            r = len(nums) - 1
            if l >= r: continue
            while l < r and number not in seen:
                value = number + nums[l] + nums[r]
                if value > 0: r -= 1
                elif value < 0: l += 1 
                elif value == 0: 
                    answer.append([number, nums[l],nums[r]])
                    l+=1
                    r-=1 
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

            seen.add(number)
        return answer
        