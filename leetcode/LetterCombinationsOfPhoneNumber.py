class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mappings, n = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }, len(digits)

        def dfs(i, comb):
            if i == n:
                return ["".join(comb)] if comb else []
            
            ret = []
            for c in mappings[digits[i]]:
                comb.append(c)
                ret.extend(dfs(i + 1, comb))
                comb.pop()
            
            return ret

        return dfs(0, [])
