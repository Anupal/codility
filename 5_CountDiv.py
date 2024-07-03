def solution(A, B, K):

    # count factors including A
    if A % K == 0:
        return (B - A) // K + 1
    # count factors excluding A - A % K
    else:
        return (B - (A - A % K)) // K
