class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dict = {}
        for word in strs:
            alphabet = [0]*26
            for letter in word:
                alphabet[ord(letter) - ord("a")] += 1
            key = tuple(alphabet)
            if key not in word_dict:
                word_dict[key] = []
            word_dict[key].append(word)

        answer = list(word_dict.values())
        return answer