class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(r, c): 
            queue = deque()
            grid[r][c] = "0"
            queue.append((r, c))
            while queue: 
                row, col = queue.popleft()
                for dr, dc in directions: 
                    nr, nc = row + dr, col + dc
                    if (nr < 0 or nr >= ROWS or 
                    nc < 0 or nc >= COLS or grid[nr][nc] == "0"): 
                        continue
                    queue.append((nr, nc))
                    grid[nr][nc] = "0"

        for r in range(ROWS): 
            for c in range(COLS): 
                if grid[r][c] == "1": 
                    bfs(r, c)
                    islands += 1

        return islands