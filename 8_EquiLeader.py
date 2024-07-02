def solution(A):
    """
    4 3 4 4 4 2
               
    :s + 1, s:
    """

    n = len(A)

    lmfreq, count, mf = [None]*n, {}, A[0]
    for i in range(n):
        count[A[i]] = count.get(A[i], 0) + 1
        
        mf = A[i] if count[mf] < count[A[i]] else mf
        
        if (i + 1) // 2 < count[mf]:
            lmfreq[i] = mf

    rmfreq, count, mf = [None]*n, {}, A[-1]
    for i in range(n - 1, -1, -1):
        count[A[i]] = count.get(A[i], 0) + 1
        
        mf = A[i] if count[mf] < count[A[i]] else mf
        
        if (n - i) // 2 < count[mf]:
            rmfreq[i] = mf

    ans = 0
    for i in range(n - 1):
        if lmfreq[i] != None and rmfreq[i + 1] != None \
            and lmfreq[i] == rmfreq[i + 1]:
                ans += 1

    return ans
