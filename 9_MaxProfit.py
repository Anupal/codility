def solution(A):
    """
    10  5 25 3 20  5  17  25  7
    """
    n, i, ans = len(A), 0, 0
    
    if n < 2: return ans

    for j in range(1, n):
        diff = A[j] - A[i]
        if diff >= 0:
            ans = max(ans, diff)
        
        else:
            i = j
    
    return ans
