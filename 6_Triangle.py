def solution(A):
    A.sort()

    for j in range(len(A) - 1, 1, -1):
        if A[j] < A[j - 1] + A[j - 2]:
            return 1

    return 0
