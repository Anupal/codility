import math

def solution(A):
    # calculate peaks
    peaks = []
    for i in range(len(A) - 2):
        if A[i] < A[i+1] > A[i + 2]:
            peaks.append(i + 1)
    num_peaks = len(peaks)
    
    # for 0-1 peaks
    if num_peaks < 2:
        return num_peaks

    # evaluate diff values of K
    ans = 0
    for K in range(2, math.isqrt(len(A)) + 2):
        flags_placed, prev = 0, None
        for peak in peaks:
            if not prev or peak - prev >= K:
                # plant flag
                flags_placed += 1
                prev = peak
            
                # out of flags
                if flags_placed == K:
                    break
        
        ans = max(ans, flags_placed)

    return ans
