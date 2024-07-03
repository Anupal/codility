def solution(A):
    n = len(A)
    A_set = set(A)

    for i in range(1, n + 1):
        if i not in A_set:
            return 0

    return 1
