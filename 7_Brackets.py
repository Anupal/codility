

def solution(S):
    fmap = {"{": "}", "[": "]", "(": ")"}
    stack = []

    for c in S:
        if c in fmap:
            stack.append(c)
        else:
            if not stack or fmap[stack[-1]] != c:
                return 0
            stack.pop()
    
    return 1 if not stack else 0


