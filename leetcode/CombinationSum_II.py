class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        count = {}
        for num in candidates: count[num] = count.get(num, 0) + 1
        keys, n = tuple(count.keys()), len(count)

        def dfs(i, total, comb):
            if total == target:
                return [tuple(comb)]
            
            if total > target or i == n:
                return []
            
            tsum, ret = total, []
            # choose 0
            ret.extend(dfs(i + 1, tsum, comb))

            # choose 1 or more
            for _ in range(count[keys[i]]):
                tsum += keys[i]
                comb.append(keys[i])
                ret.extend(dfs(i + 1, tsum, comb))
            
            # pop
            for _ in range(count[keys[i]]):
                comb.pop()
            
            return ret
    
        return dfs(0, 0, [])
            
            
