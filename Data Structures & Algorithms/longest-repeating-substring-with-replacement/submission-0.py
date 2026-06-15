class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        [a,a,a,b,b] k = 1
           ^     ^
        """
        l = 0
        r = 1
        seen = defaultdict(int)
        max_letter = 0
        res = 0
        for r in range(len(s)):
            seen[s[r]] += 1
            max_letter = max(max_letter, seen[s[r]])
            while (r - l + 1) - max_letter > k:
                seen[s[l]] -= 1
                l += 1
                max_letter = max(seen.values())
            res = max(res, r - l + 1)
        
        return res


            



        