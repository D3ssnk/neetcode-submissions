class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s = defaultdict(int)
        for n in nums:
            s[n] += 1
        sl = list(s.keys())
        sl = sorted(sl, key=lambda x: -s[x])
        
        return sl[:k]
        