# https://codesays.com/2014/solution-to-max-slice-sum-by-codility/

def solution(A):
    """
    [3, 2, -6, 4, 0]
    [3, 2, -3, 9, 0]
    [-1, -2, -3]
    [1, 2]
    [-1, 2]
    [3, -1, 2]
    [-2, -1]
    [0, 0, 3]
    [1, 2, 3]
    [11, -5, 2]
    [11, -5, 8]

    net sum should be positive, otherwise break after negative integer
    """
    n, ans, current_sum = len(A), A[0], A[0]

    for i in range(1, n):
        # reset if after adding the sum is less than the element itself
        current_sum = max(A[i], current_sum + A[i])
        ans = max(ans, current_sum)

    return ans
