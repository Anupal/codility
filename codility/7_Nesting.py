def solution(S):
    stack = 0
    for c in S:
        if c == "(":
            stack += 1
        else:
            if stacki == 0:
                return 0
            else:
                stack -= 1
    
    return 0 if stack else 1
