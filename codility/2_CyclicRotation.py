def solution(A, K):
    """
     0  1  2  3  4
    [3, 8, 9, 7, 6]

    [9, 7, 6, 3, 8]
    
    K = 3
    """
    n = len(A)
    
    # edge cases
    if n < 2:
        return A
    
    # mod K to prevent looping wastage
    K, ans = K % n, [0] * n

    # rotate by pivoting
    for i in range(n):
        ans[(i + K) % n] = A[i]
    
    return ans
