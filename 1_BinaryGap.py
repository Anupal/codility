def solution(N):
    N_bin = bin(N).lstrip("0b").rstrip("0")

    seq, ans, n = 0, 0, len(N_bin)
    for i in range(n):
        if N_bin[i] == "0":
            if seq:
                seq += 1
            else:
                seq = 1
        else:
            if seq:
                ans = max(ans, seq)
                seq = 0
    
    return ans
