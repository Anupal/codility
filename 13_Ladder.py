def solution(A, B):
    """
    0 1 2 3 4 5 6
    1 2 3 5  (fib series)
    """

    n, max_step, max_mod = len(A), max(A), max(B)

    # gen fib cache
    fibs = [1, 2] + [-1] * (max_step - 2)
    for l in range(2, max_step):
        fibs[l] = (fibs[l - 1] + fibs[l - 2]) % 2 ** max_mod

    return [fibs[A[i] - 1] % 2 ** B[i] for i in range(n)]
