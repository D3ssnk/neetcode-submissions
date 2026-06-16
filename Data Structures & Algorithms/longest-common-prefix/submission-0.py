class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        for i,letter in enumerate(min(strs)):
            contains_letter = True
            for word in strs:
                if word[i] != letter:
                    contains_letter = False
                    break
            if contains_letter:
                res += letter
            else:
                break

        return res