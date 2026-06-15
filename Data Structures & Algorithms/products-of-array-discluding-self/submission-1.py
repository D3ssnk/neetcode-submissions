class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l2r = [1]*(len(nums)+1)
        r2l = [1]*(len(nums)+1)
        for n in range(1,len(nums)+1,1):
            l2r[n] = l2r[n-1]*nums[n-1]
            r2l[n] = r2l[n-1]*nums[::-1][n-1]
        
        l2r = l2r[:-1]
        r2l = r2l[:-1][::-1]
        answer = [l2r[n] * r2l[n] for n in range(len(r2l))]
        return answer