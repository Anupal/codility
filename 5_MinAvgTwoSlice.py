# basic prefix sum - slow - O(n^2)
def solution(A):
    """
    logic:

    4  2  2  5  1  5  8
    rolling sum optimization applies here
    """
    n = len(A)
    rsum = [0] * (n + 1)
    rsum[0] = A[0]
    for i in range(1, n):
        rsum[i] = rsum[i - 1] + A[i]
    
    ans_i, ans_avg = 0, float("inf")

    for i in range(n):
        for j in range(i + 1, n):
            avg = (rsum[j] - rsum[i - 1]) / (j - i + 1)
            if avg < ans_avg:
                ans_i = i
                ans_avg = avg
            elif avg == ans_avg and i < ans_i:
                ans_i = i
    
    return ans_i

# basic prefix sum - 2/3 slice - O(3n)
def solution(A):
    """
    logic:

    4  2  2  5  1  5  8
    * rolling sum optimization applies here
    * min avg slice will not have 2 - 3 size
    """
    n = len(A)
    rsum = [0] * (n + 1)
    rsum[0] = A[0]
    for i in range(1, n):
        rsum[i] = rsum[i - 1] + A[i]

    ans_i, ans_avg = 0, float("inf")

    for i in range(n):
        for j in range(i + 1, i + 3):
            if j >= n:
                continue
            avg = (rsum[j] - rsum[i - 1]) / (j - i + 1)
            if avg < ans_avg:
                ans_i = i
                ans_avg = avg
            elif avg == ans_avg and i < ans_i:
                ans_i = i

    return ans_i


