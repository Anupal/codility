
# sorting (nlogn)
def solution(A):
    """
    1, 1, 2, 3, 4, 6
    """
    A.sort()
    ans = 1
    for i in range(len(A)):
        if A[i] <= 0:
            continue
        if A[i] == ans:
            ans += 1
        
        if A[i] > ans:
            break
    
    return ans

# using occurence
def solution(A):
    """
    If the size of array is N,
    the max num that can be the answer is N + 1
    that is when all elments 1 -> N are present.
    The answer cannot be larger than this.
    """

    occurence = [False] * (len(A) + 1)

    for a in A:
        if 0 < a < len(A) + 1:
            occurence[a - 1] = True

    for i in range(len(A) + 1):
        if not occurence[i]:
            return i + 1
