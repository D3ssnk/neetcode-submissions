class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(i,total,stack):
            if total == target:
                res.append(stack.copy())
                return
            
            for n in range(i, len(candidates)):
                if n > i and candidates[n] == candidates[n - 1]:
                    continue
                if total + candidates[n] > target:
                    break
                stack.append(candidates[n])
                backtrack(n+1, total + candidates[n],stack)
                stack.pop()

        backtrack(0,0,[])
        return res        

        