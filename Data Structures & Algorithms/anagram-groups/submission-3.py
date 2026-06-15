class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for n in strs:
            letters = [0]*26
            for m in n:
                letters[ord(m) - ord('a')] += 1
            ans[tuple(letters)].append(n)
        
        return list(ans.values())


        