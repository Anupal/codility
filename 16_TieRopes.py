def solution(K, A):
    """
    1  2  3  4  1  1  3
    
    compute rolling sums

    edge cases when last indices don't add up to >= K
    [4, [1, 1, 1, 1, 4, 5, 2, 3, 1]]
    [4, [1, 1, 1, 1, 4, 5, 2, 3, 1, 3]]
    [4, [1, 1, 1, 1, 4, 5, 2, 3, 1, 2]]

    """
    i, n, ropes = 0, len(A), 0

    while i < n:
        j, rsum = i + 1, A[i]

        while j < n and rsum < K:
            rsum += A[j]
            j += 1
        
        if rsum >= K:
            ropes += 1
        i = j
    
    return ropes
