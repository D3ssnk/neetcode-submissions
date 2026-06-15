class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        seen = set()
        res = []
        stack = []

        def backtrack(i):
            print(stack)
            if sum(stack) == target:
                if tuple(stack) not in seen:
                    res.append(stack.copy())
                    seen.add(tuple(stack))
                return
            if sum(stack) > target or i >= len(candidates):
                return
            
            stack.append(candidates[i])
            backtrack(i+1)

            stack.pop()
            backtrack(i+1)

        backtrack(0)
        return res        

        