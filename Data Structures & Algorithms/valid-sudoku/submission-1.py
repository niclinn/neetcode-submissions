class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(ROWS): 
            for c in range(COLS): 
                num = board[r][c]

                if num == ".": 
                    continue
                
                if num in rows[r]: 
                    return False
                else: 
                    rows[r].add(num)

                if num in cols[c]: 
                    return False
                else: 
                    cols[c].add(num)

                if num in boxes[(r // 3, c // 3)]: 
                    return False
                else: 
                     boxes[(r // 3, c // 3)].add(num)

        return True