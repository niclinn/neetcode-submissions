class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(len(board)): 
            for c in range(len(board[r])): 
                digit = board[r][c]
                if digit == '.': 
                    continue
                
                if digit in rows[r]: 
                    return False
                else: 
                    rows[r].add(digit)
                
                if digit in cols[c]: 
                    return False
                else: 
                    cols[c].add(digit)
                
                if digit in boxes[(r // 3, c // 3)]: 
                    return False
                else: 
                    boxes[(r // 3, c // 3)].add(digit)
                
        return True