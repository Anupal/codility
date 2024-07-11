def solution(A):
    """
    Given an array A, this function returns the number of triangular 
    triplets in the array.
    
    i ----------
    j  ----------
    k   ----------
    """
    A.sort()
    n = len(A)
    count = 0
    
    # Iterate over the array, considering each element as the largest 
    # side of the triangle
    for i in range(n - 2):
        k = i + 2
        for j in range(i + 1, n - 1):
            while k < n and A[i] + A[j] > A[k]:
                k += 1
            count += k - j - 1
            
    return count
