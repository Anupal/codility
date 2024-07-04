def solution(A):
    """
    Remember next peak for every index
    """
    n = len(A)
    prev, next_peak, num_peaks = None, [None] * n, 0
    for i in range(n - 2, 0, -1):
        # this is a peak
        if A[i - 1] < A[i] > A[i + 1]:
            prev = i
            num_peaks += 1
        next_peak[i] = prev
    next_peak[0] = prev

    if num_peaks < 2:
        return num_peaks
    
    # iterate over different sizes of the split
    for split in range(2, n // 2 + 1):
        # split if valid only if it is divisor of N
        if n % split != 0:
            continue
        valid = True
        for k in range(0, n, split):
            if next_peak[k] == None or next_peak[k] >= k + split:
                valid = False
                break
        
        if valid:
            return n // split
    
    # if no split size is valid then only one block (whole array)
    return 1
