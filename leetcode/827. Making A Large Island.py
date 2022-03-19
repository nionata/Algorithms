class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n, counts = len(grid), {}
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    idx = len(counts)+2
                    c = self.dfs(grid, copy, n, i, j, idx)
                    counts[idx] = c
        largest = max(counts.values() or [0])
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    c = 0
                    seen = {}
                    for a, b in [(0,-1), (-1,0), (1,0), (0,1)]:
                        x, y = i+a, j+b
                        in_bounds = 0 <= x < n and 0 <= y < n
                        if not in_bounds or grid[x][y] < 2:
                            continue
                        idx = grid[x][y]
                        if idx in seen:
                            continue
                        c += counts[idx]
                        seen[idx] = True
                    largest = max(largest, c+1)
        return largest
        
    def dfs(self, grid: List[List[int]], copy: List[List[int]], n, i, j, idx) -> int:
        c = 1
        grid[i][j] = idx
        for a, b in [(0,-1), (-1,0), (1,0), (0,1)]:
            x, y = i+a, j+b
            in_bounds = 0 <= x < n and 0 <= y < n
            if not in_bounds or grid[x][y] != 1:
                continue 
            c += self.dfs(grid, copy, n, x, y, idx)
        return c
