class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        
        def dfs(i, subset):
            if i == n:
                return [tuple(subset)]
            
            ret = []
            subset.append(nums[i])
            ret.extend(dfs(i + 1, subset))
            subset.pop()
            ret.extend(dfs(i + 1, subset))

            return ret
        
        return dfs(0, [])
