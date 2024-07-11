class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        count = {}
        for num in nums: count[num] = count.get(num, 0) + 1
        keys = tuple(count.keys())
        n = len(count)

        def dfs(i, subset):
            if i == n:
                return [tuple(subset)]
            
            ret = []
            # choose 1 or more
            for _ in range(count[keys[i]]):
                subset.append(keys[i])
                ret.extend(dfs(i + 1, subset))
            
            # pop
            for _ in range(count[keys[i]]):
                subset.pop()
            
            # choose 0
            ret.extend(dfs(i + 1, subset))

            return ret
        
        return dfs(0, [])
