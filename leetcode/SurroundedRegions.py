class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.

        Backtrace from edges and mark them edgebound.
        Convert all O cells which are not edgebound as X.
        """

        m, n = len(board), len(board[0])
        steps = ((1, 0), (-1, 0), (0, 1), (0, -1))
        edgebound = set()

        def mark(i, j):
            if (
                0 <= i < m
                and 0 <= j < n
                and (i, j) not in edgebound
                and board[i][j] == "O"
            ):
                edgebound.add((i, j))
                for di, dj in steps:
                    mark(i + di, j + dj)

        # left & right
        for i in range(m):
            mark(i, 0)
            mark(i, n - 1)

        # top & bottom
        for j in range(n):
            mark(0, j)
            mark(m - 1, j)

        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if board[i][j] == "O" and (i, j) not in edgebound:
                    board[i][j] = "X"
