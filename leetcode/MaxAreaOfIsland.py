class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        steps = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and not visited[i][j] and grid[i][j] == 1:
                visited[i][j] = True
                ret = 1
                for di, dj in steps:
                    ret += dfs(i + di, j + dj)
                return ret

            return 0

        max_island = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] and not visited[i][j]:
                    max_island = max(max_island, dfs(i, j))

        return max_island
