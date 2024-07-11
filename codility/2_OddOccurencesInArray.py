def solution(A):
    n = len(A)
    
    visited = set()
    for i in range(n):
        if A[i] in visited:
            visited.remove(A[i])
        else:
            visited.add(A[i])

    return visited.pop()
