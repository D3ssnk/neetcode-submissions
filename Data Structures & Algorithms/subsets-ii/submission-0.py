class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        nums.sort()
        for num in nums:
            res += [subset + [num] for subset in res]
        
        seen = set()
        ans = []
        for array in res:
            item = tuple(array)
            if item not in seen:
                ans.append(list(item))
            seen.add(item)

        return ans
        