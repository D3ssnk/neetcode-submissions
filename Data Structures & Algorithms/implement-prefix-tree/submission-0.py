class PrefixTree:

    def __init__(self):
        self.stack = []
        

    def insert(self, word: str) -> None:
        self.stack.append(word)

    def search(self, word: str) -> bool:
        for s in self.stack:
            if s == word: return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        for s in self.stack:
            if s.find(prefix) == 0: return True
        return False
        
        