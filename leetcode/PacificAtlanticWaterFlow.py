class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        Trace flow in reverse from the edges and save the traced cells in pacific or atlantic.
        Then loop through all cells and save the cells which are in both pacific and atlantic.
        """
        m, n = len(heights), len(heights[0])
        a_cells, p_cells, visited = set(), set(), set()
        steps = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def backtrace(i, j, visited, prev):
            if (
                0 <= i < m
                and 0 <= j < n
                and (i, j) not in visited
                and prev <= heights[i][j]
            ):
                visited.add((i, j))
                for di, dj in steps:
                    backtrace(i + di, j + dj, visited, heights[i][j])

        # left right
        for i in range(m):
            backtrace(i, 0, p_cells, heights[i][0])
            backtrace(i, n - 1, a_cells, heights[i][n - 1])

        # top, bottom
        for j in range(n):
            backtrace(0, j, p_cells, heights[0][j])
            backtrace(m - 1, j, a_cells, heights[m - 1][j])

        ans = []
        for i in range(m):
            for j in range(n):
                if (i, j) in a_cells and (i, j) in p_cells:
                    ans.append((i, j))

        return ans
