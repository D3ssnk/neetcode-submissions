class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        array_a = [0]*26
        array_b = [0]*26
        for n in range(len(s)):
            array_a[ord(s[n]) - ord('a')] += 1
            array_b[ord(t[n]) - ord('a')] += 1 
        
        if array_a != array_b: return False
        else: return True

        