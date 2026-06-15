class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.stack = nums
        self.index = k
        

    def add(self, val: int) -> int:
        self.stack.append(val)
        self.stack = sorted(self.stack)[::-1]
        return self.stack[self.index - 1]
        
