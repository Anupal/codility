def solution(X, A):
    leaves = {x for x in range(1, X + 1)}

    for i in range(len(A)):
        if A[i] in leaves:
            leaves.remove(A[i])

            if not leaves:
                return i
    
    return -1
