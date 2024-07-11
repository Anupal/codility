class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)

        def is_palindrome(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i , j = i + 1, j - 1
            return True

        ans, parts = [], []

        def dfs(i):
            if i == n:
                ans.append(tuple(parts))
                return

            for j in range(i, n):
                if is_palindrome(i, j):
                    parts.append(s[i:j + 1])
                    dfs(j + 1)
                    parts.pop()
        
        dfs(0)
        return ans

