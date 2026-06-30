class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rs = defaultdict(set)
        cs = defaultdict(set)
        ss = defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                
                if val in rs[r] or val in cs[c] or val in ss[(r//3,c//3)]:
                    print(rs,cs,ss)
                    return False
                else:
                    rs[r].add(val)
                    cs[c].add(val)
                    ss[(r//3,c//3)].add(val)
        
        return True
