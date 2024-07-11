class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)

        def dfs(i, comb, total):
            if total == target:
                return [tuple(comb)]
            
            if i == n or total > target:
                return []

            ret = []
            comb.append(candidates[i])
            ret.extend(dfs(i, comb, total + candidates[i]))
            comb.pop()
            ret.extend(dfs(i + 1, comb, total))

            return ret
        
        return dfs(0, [], 0)
