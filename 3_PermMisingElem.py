def solution(A):
    n = len(A)
    visited = {i for i in range(1, n + 2)}

    for e in A:
        visited.remove(e)

    return visited.pop()
