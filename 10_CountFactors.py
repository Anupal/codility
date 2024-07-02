def solution(N):
    i, ans = 1, 0
    
    # check 1 to root N, increment by 2 as it includes both divs
    while i * i < N:
        if N % i == 0:
            ans += 2
        i += 1
    
    # in case the number has a square root
    if i * i == N:
        ans += 1

    return ans
