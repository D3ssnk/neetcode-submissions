class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)
        for word in strs:
            array = [0]*26
            for letter in word:
                array[ord(letter)- ord('a')] += 1
            anagram[tuple(array)].append(word)
        
        return list(anagram.values())
