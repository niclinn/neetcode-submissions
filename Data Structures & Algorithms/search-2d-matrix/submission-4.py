class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 1. binary search the cols
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bottom = 0, ROWS - 1
        while top <= bottom: 
            m = (top + bottom) // 2
            # row is beyond
            if matrix[m][-1] < target: 
                top = m + 1
            # row is below
            elif matrix[m][0] > target: 
                bottom = m - 1
            else: 
                break
        
        if top > bottom: return False

        left, right = 0, COLS - 1
        row = m

        nums = matrix[row]

        while left <= right: 
            m = (left + right) // 2
            if nums[m] > target: 
                right = m - 1
            elif nums[m] < target: 
                left = m + 1
            else: 
                return True
        return False

