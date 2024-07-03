def solution(X, Y, D):
    div = (Y - X) // D
    rem = (Y - X) % D

    return div + (1 if rem else 0)
