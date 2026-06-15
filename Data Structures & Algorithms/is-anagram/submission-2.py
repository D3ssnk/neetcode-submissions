class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        s_array = [0]*26
        t_array = [0]*26
        
        for n in range(len(s)):
            s_array[ord(s[n])-ord('a')] += 1
            t_array[ord(t[n])-ord('a')] += 1
        
        return s_array == t_array

        