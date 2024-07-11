class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        steps = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def mark_visited(i, j):
            if 0 <= i < m and 0 <= j < n and not visited[i][j] and grid[i][j] == "1":
                visited[i][j] = True
                for di, dj in steps:
                    mark_visited(i + di, j + dj)
        
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not visited[i][j]:
                    count += 1
                    mark_visited(i, j)

        return count
