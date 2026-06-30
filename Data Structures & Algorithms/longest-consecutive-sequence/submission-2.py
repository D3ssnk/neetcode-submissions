class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        number_chain = defaultdict(lambda: None)
        largest = 0

        for num in nums:
            number_chain[num] = 1
            if number_chain[num - 1] is not None:
                print("did")
                number_chain[num] += number_chain[num - 1]
            i = num
            while number_chain[i + 1] is not None:
                i += 1
            if i != num:
                number_chain[i] += number_chain[num]
            
            largest = max(number_chain[i],largest,number_chain[num])
        
        return largest 
        
        
        