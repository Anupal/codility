# https://codesays.com/2014/solution-to-max-double-slice-sum-by-codility/

def solution(A):
    """
    3 2 6 -1 4 5 -1 2

    1 2 3

    1 2 3 4

    x <---> y <---> z
    """
    # find sequences which end at a particular index
    n = len(A)
    endings, current_sum = [0] * n, 0
    for i in range(1, n - 2):
        current_sum = max(0, current_sum + A[i])
        endings[i] = current_sum
    
    # find sequences which begin at a particular index
    beginnings, current_sum = [0] * n, 0
    for i in range(n - 2, 1, -1):
        current_sum = max(0, current_sum + A[i])
        beginnings[i] = current_sum
    
    # get max sum of sequences
    ans = 0
    for i in range(n - 2):
        ans = max(ans, endings[i] + beginnings[i + 2])

    return ans
