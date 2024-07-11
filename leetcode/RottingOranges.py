class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rotten = [[0 for _ in range(n)] for _ in range(m)]
        steps = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def dfs(i, j, level):
            """
            Explore is unvisited (rotten = 0) or better exploration (current level is < rotten)
            """
            if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                if rotten[i][j] == 0 or level < rotten[i][j]:
                    rotten[i][j] = level
                    for di, dj in steps:
                        dfs(i + di, j + dj, level + 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    for di, dj in steps:
                        dfs(i + di, j + dj, 1)

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not rotten[i][j]:
                    return -1
                ans = max(ans, rotten[i][j])

        return ans
