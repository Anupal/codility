def solution(A):
    """
    0  1  0  1  1
    >  <  >  <  <
    """

    n, ecars = len(A), 0

    i = 0
    while i < n and A[i] == 1:
        i += 1
    
    passing_cars = 0
    while i < n:
        if A[i] == 0:
            ecars += 1
        else:
            passing_cars += ecars

        i += 1

        if passing_cars > 1_000_000_000:
            return -1
    
    return passing_cars
