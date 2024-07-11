def solution(A):
    """
    4  3  4  4  4  2

    lets say we have i = 4
    with elements 1 1 2 2 3
    l = 5, the count of most frequent should be more than half,
    otherwise it means that multiple elements have mf count
    
    counter eg: 1 1 1 2 3 here count(1) = 3 > 2.5, no other element
    can be equal to this.
    """
    n = len(A)
    rleaders = [None] * n

    count, mf = {}, A[-1]
    for i in range(n - 1, -1, -1):
        count[A[i]] = count.get(A[i], 0) + 1
        if count[A[i]] > count[mf]:
            mf = A[i]

        if (n - i) // 2 < count[mf]:
            rleaders[i] = mf
        
    lleaders = [None] * n
    count, mf = {}, A[0]
    for i in range(n):
        count[A[i]] = count.get(A[i], 0) + 1
        if count[A[i]] > count[mf]:
            mf = A[i]
        
        if (i + 1) // 2 < count[mf]:
            lleaders[i] = mf
    
    ans = 0
    for i in range(n - 1):
        if lleaders[i] != None and rleaders[i + 1] != None \
        and lleaders[i] == rleaders[i + 1]:
            ans += 1
    return ans
