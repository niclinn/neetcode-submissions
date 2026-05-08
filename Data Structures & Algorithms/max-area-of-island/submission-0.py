class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        area = 0
        
        def dfs(r, c): 
            grid[r][c] = 0
            size = 1
            for dr, dc in directions: 
                nr, nc = r + dr, c + dc
                if (nr >= 0 and nr < ROWS and nc >= 0 and nc < COLS
                and grid[nr][nc] == 1): 
                    size += dfs(nr, nc)
            return size

        for r in range(ROWS): 
            for c in range(COLS): 
                if grid[r][c] == 1: 
                    area = max(area, dfs(r, c))
        
        return area

