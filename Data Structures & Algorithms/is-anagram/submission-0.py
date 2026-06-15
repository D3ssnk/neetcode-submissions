class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word1 = [0]*26
        word2 = [0]*26
        if len(s) != len(t):
            return False
        
        for n in range(len(s)):
            word1[ord(s[n]) - ord("a")] += 1
            word2[ord(t[n]) - ord("a")] += 1

        if word1 == word2:
            return True
        else:
            return False