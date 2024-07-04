def solution(A):
    """
    idealy max product will be of largest elements
    after sorting
    p p p p p
        -----
    n n n n n
        -----
    n n n n p

    n n n p p
    

    -4 -3 -2 2 3
    largest positives will be on right
    largest negatives will be on left
    """
    A.sort()

    return max(A[-1] * A[-2] * A[-3], A[0] * A[1]* A[-1])
