class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, size = len(grid), 0
        m = len(grid[0]) if n > 0 else 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    size = max(size, self.dfs(grid, i, j, n, m))
        return size     
        
    def dfs(self, grid, i, j, n, m):
        size = 1
        grid[i][j] = 0
        for a, b in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
            x, y = i+a, j+b
            in_bounds = 0 <= x < n and 0 <= y < m
            if not in_bounds or grid[x][y] != 1:
                continue
            size += self.dfs(grid, x, y, n, m)
        return size
