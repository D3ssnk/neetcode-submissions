class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nc = defaultdict(int)

        for num in nums:
            nc[num] += 1

        ans = [n for n in nc.keys() if nc[n] > len(nums)/3] 
        return ans
        