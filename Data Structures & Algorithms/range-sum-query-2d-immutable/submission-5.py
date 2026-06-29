class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        for r in range(rows):
            for c in range(cols):
                if r - 1 >= 0:
                    matrix[r][c] += matrix[r - 1][c]
                if c - 1 >= 0:
                    matrix[r][c] += matrix[r][c - 1]
                if r - 1 >= 0 and c - 1 >= 0:
                    matrix[r][c] -= matrix[r - 1][c - 1]
        print(matrix)
        self.matrix = matrix
        

        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if col1 - 1 < 0 and row1 - 1 < 0:
            return self.matrix[row2][col2]
        if row1 - 1 < 0:
            return self.matrix[row2][col2] - self.matrix[row2][col1 - 1]
        if col1 - 1 < 0:
            return self.matrix[row2][col2] - self.matrix[row1 - 1][col2]
        
    
        return self.matrix[row2][col2] - self.matrix[row2][col1 - 1] - self.matrix[row1 - 1][col2] + self.matrix[row1 - 1][col1 - 1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)