# https://stackoverflow.com/questions/4801242/algorithm-to-calculate-number-of-intersecting-discs

def solution(A):
    def binary_search(x, target):
        """
        finds index of x[i][0] which is <= target
        """
        i, j = 0, len(x)
        while i < j:
            m = (i + j) // 2
            if x[m][0] <= target:
                i = m + 1
            else:
                j = m
        
        return i

    n = len(A)
    disks = [(i - A[i], i + A[i]) for i in range(n)]
    disks.sort()

    pairs = 0
    for i in range(n):
        count = binary_search(disks, disks[i][1])
        count -= i + 1
        pairs += count
        if pairs > 10_000_000:
            return -1

    return pairs
