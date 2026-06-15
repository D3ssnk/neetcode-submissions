class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1 
        r = max(piles)
        answer = float("inf")
        while l <= r:
            m = (l + r) // 2
            placeholder = 0
            for pile in piles:
                placeholder += math.ceil(pile/m)
            if placeholder > h: l = m + 1
            elif placeholder <= h: 
                answer = min(m, answer)
                r = m - 1 



        return answer

        