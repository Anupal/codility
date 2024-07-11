def solution(A):
    """
    2  3  1  5  8  1  10
    """
    ans, n, i = 0, len(A), 0
    for j in range(1, n):
        if A[j] < A[i]:
            i = j
        else:
            ans = max(ans, A[j] - A[i])
    return ans
