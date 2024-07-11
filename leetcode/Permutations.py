class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(visited, perm):
            if len(perm) == len(nums):
                return [tuple(perm)]

            ret = []
            for n in nums:
                if n in visited:
                    continue
                
                perm.append(n)
                visited.add(n)
                ret.extend(dfs(visited, perm))
                perm.pop()
                visited.remove(n)
            
            return ret
        
        return dfs(set(), [])

