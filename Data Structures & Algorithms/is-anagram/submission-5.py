class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not len(s) == len(t):
            return False
        
        s_arr = [0] * 26
        t_arr = [0] * 26

        for i in range(len(t)):
            s_arr[ord(s[i]) - ord('a')] += 1
            t_arr[ord(t[i]) - ord('a')] += 1 

        return t_arr == s_arr


        