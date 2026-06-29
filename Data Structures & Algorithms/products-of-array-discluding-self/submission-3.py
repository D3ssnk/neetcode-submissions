class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        reverse_nums = reversed(nums)
        product_forward = []
        product_backwards = []

        pf = 1
        pb = 1
        for num in nums:
            pf *= num
            product_forward.append(pf)
        product_forward = product_forward[:-1]
        product_forward.reverse()
        product_forward.append(1)
        product_forward.reverse()

        for num in reverse_nums:
            pb *= num
            product_backwards.append(pb)
        product_backwards = product_backwards[:-1]
        product_backwards.reverse()
        product_backwards.append(1)

        final = []
        for n, m in zip(product_backwards,product_forward):
            final.append(n*m)
        
        return final 



        