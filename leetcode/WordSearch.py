class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n, o = len(board), len(board[0]), len(word)
        visited = [[False for _ in range(n)] for _ in range(m)]
        steps = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def dfs(i, j, k):
            if k == o:
                return True
            if 0 <= i < m and 0 <= j < n and k < o and not visited[i][j] and board[i][j] == word[k]:
                visited[i][j] = True
                for di, dj in steps:
                    if dfs(i + di, j + dj, k + 1):
                        return True
                visited[i][j] = False
            
            return False
        
        # check for all cells
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        
        return False
