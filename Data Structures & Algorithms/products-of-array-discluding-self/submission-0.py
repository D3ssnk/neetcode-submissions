class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_lr = [1]
        product_rl = [1]
        for n in range(len(nums) - 1):
            product_lr.append(product_lr[-1] * nums[n])
        
        nums_r = nums[::-1]
        for n in range(len(nums) - 1):
            product_rl.append(product_rl[-1] * nums_r[n])

        product_rl = product_rl[::-1]
        
        answer = []
        for n in range(len(product_rl)):
            product = product_rl[n] * product_lr[n]
            answer.append(product) 
        return answer
            
            
        