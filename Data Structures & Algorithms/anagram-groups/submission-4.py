class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for word in strs:
            word_arr = [0]*26
            for letter in word:
                word_arr[ord(letter) - ord('a')] += 1
            res[tuple(word_arr)].append(word)
        
        return list(res.values())
