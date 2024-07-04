def solution(A):
    """
    After sorting,
    if sum of next two largest cannot exceed largest then
    shift left
    because if condition holds true the other sum comparisons will also
    hold true since largest is anyway bigger than other two individually.
    """
    A.sort()

    for i in range(len(A) - 1, 1, -1):
        if A[i] < A[i - 1] + A[i - 2]:
            return 1
    return 0
