class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for number in nums:
            if number not in dic:
                dic[number] = 0
            dic[number] += 1
            if dic[number] > 1:
                return True
        
        return False 
         