class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        l = 0
        r = rows * cols 
    
        while l <= r:
            m = (l + r) // 2
            m_rows = m // cols
            m_cols = m % cols
            if m_rows == len(matrix): break  
            if matrix[m_rows][m_cols] < target: l = m + 1
            elif matrix[m_rows][m_cols] > target: r = m - 1
            elif matrix[m_rows][m_cols] == target: return True

        return False 

        