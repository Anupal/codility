def solution(A):
    """
    n n n n n n
            - -
    n n n p p p
    ->  - -  <-

    -8 -7      7 11
    
    p p p p p p
    - -
    
    1  4  -3

    -8  4  5  -10  3

    -3  1  4

    -10  -8  3  4  5
    """
    n = len(A)
    A.sort()
    if n == 1:
        return 2 * abs(A[0])

    # all positive
    if A[0] >= 0:
        return min(2 * A[0], A[0] + A[1])

    # all negative
    if A[-1] < 0:
        return min(2 * abs(A[-1]), abs(A[-1] + A[-2]))
    
    # mix
    else:
        ans = float("inf")
        i, j = 0, n - 1
        while i <= j:
            ans = min(ans, abs(A[i] + A[j]))

            # different signs
            if A[i] ^ A[j] < 0:
                if abs(A[i]) > abs(A[j]):
                    i += 1
                else:
                    j -= 1
            # converged to same signs
            else:
                ans = min(ans, 2 * abs(A[i]), 2 * abs(A[j]))
                break
    
    return ans

