def solution(M, A):
    """
    arr: 3  4  5  6  2
    inc: 1  2  3  4
    every new added index will have slice with all existing ones
    to left + solo slice of itself.

    keep removing elements from window until it matches new element

    1 2 3 4 1
    """
    i, window, distinct = 0, {A[0]}, 1
    for j in range(1, len(A)):
        if A[j] in window:
            while A[i] != A[j]:
                window.remove(A[i])
                i += 1
            i += 1
        else:
            window.add(A[j])
        distinct += (j - i + 1)
        
        if distinct > 1_000_000_000:
            return 1_000_000_000
    
    return distinct
