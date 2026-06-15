class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        seen = set()
        ans = False
        def backtracking(r,c,i):
            if i == len(word): return True

            if r >= len(board) or c >= len(board[0]) or min(r,c) < 0 or (r,c) in seen:
                return

            if word[i] != board[r][c]: 
                return
            
            seen.add((r,c))
            res = (backtracking(r+1,c,i+1) or
            backtracking(r-1,c,i+1) or
            backtracking(r,c+1,i+1) or
            backtracking(r,c-1,i+1))
            seen.remove((r,c))
            return res
        
        for r in range(len(board)):
            if ans: break
            for c in range(len(board[0])):
                ans = backtracking(r,c,0)
                print(ans)
                if ans: break
        
        return ans if ans else False
        


            



