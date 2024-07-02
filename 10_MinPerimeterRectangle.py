import math

def solution(N):
    i, perimeter = 1, float("inf")

    a = math.isqrt(N)
    if a * a == N:
        return 4 * a

    while i * i < N:
        if N % i == 0:
            a, b = i, N // i
            perimeter = min(perimeter, 2 * (a + b))
        
        i += 1
    
    return perimeter
