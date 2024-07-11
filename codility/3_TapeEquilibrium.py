def solution(A):
    """
    3  1  2  4  3
    3  4  6 10 13
   13 10  9  7  3
    """
    n = len(A)
    rsum = [A[-1]] * n
    for i in range(n - 2, -1, -1):
        rsum[i] = rsum[i + 1] + A[i]
    
    lsum, ans = A[0], float("inf")
    for i in range(1, n):
        ans = min(abs(lsum - rsum[i]), ans)
        lsum += A[i]

    return ans
