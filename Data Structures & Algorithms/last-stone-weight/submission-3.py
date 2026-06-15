class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = abs(heapq.heappop(stones))
            second = abs(heapq.heappop(stones))

            if first > second: stone = -(first - second)
            else: stone = 0

            if stone != 0:
                heapq.heappush(stones, stone)
        
        return abs(heapq.heappop(stones)) if stones else 0

        