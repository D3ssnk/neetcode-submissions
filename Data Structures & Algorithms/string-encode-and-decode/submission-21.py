class Solution:
    def __init__(self):
        self.decode_list = []

    def encode(self, strs: List[str]) -> str:
        self.decode_list = strs
        return " ".join(strs)

    def decode(self, s: str) -> List[str]: 

        return self.decode_list
