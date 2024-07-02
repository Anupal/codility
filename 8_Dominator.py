def solution(A):
    count, n = {}, len(A)
    h = n // 2

    for i in range(n):
        count[A[i]] = count.get(A[i], 0) + 1
        if count[A[i]] > h:
            return i
    
    return -1
