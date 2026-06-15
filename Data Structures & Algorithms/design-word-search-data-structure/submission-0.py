class WordDictionary:

    def __init__(self):
        self.stack = []
        

    def addWord(self, word: str) -> None:
        self.stack.append(word)
        

    def search(self, word: str) -> bool:
        for s in self.stack:
            count = 0
            if len(s) == len(word):
                for n in range(len(word)):
                    if word[n] == "." or word[n] == s[n]: count += 1
                    else: break
                    print(word, s, count)
                if count == len(word): return True
        
        return False
        
